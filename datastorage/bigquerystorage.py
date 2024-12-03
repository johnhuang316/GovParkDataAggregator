import os
import string
from dataclasses import asdict, dataclass
from google.cloud import bigquery
from dto.parkingdata import ParkingData
from .idatastorage import IDataStorage
from .bigquerytableschema import TableSchema
from utils.logger import logger


@dataclass
class BigQueryStorage(IDataStorage):
    client: bigquery.Client = None

    def __post_init__(self):
        logger.debug("Initializing BigQuery client")
        self.client = bigquery.Client()

    def create_table(self, table_schema: TableSchema):
        table_id = self.__get_table_id(table_schema.table_name)
        schema = table_schema.get_create_table_schema()
        logger.info(f"Creating table: {table_id}")

        try:
            table = bigquery.Table(table_id, schema=schema)
            table = self.client.create_table(table)
            logger.info(f"Successfully created table {table.project}.{table.dataset_id}.{table.table_id}")
        except Exception as e:
            logger.error(f"Failed to create table {table_id}: {str(e)}")
            raise

    def insert_data(self, table_name: string, datas: list[ParkingData]):
        table_id = self.__get_table_id(table_name)
        logger.info(f"Inserting {len(datas)} records into {table_id}")

        try:
            errors = self.client.insert_rows_json(
                table_id, [asdict(data) for data in datas], row_ids=[None] * len(datas))

            if not errors:
                logger.info(f"Successfully inserted {len(datas)} rows into {table_id}")
            else:
                error_msg = f"Encountered errors while inserting into {table_id}: {errors}"
                logger.error(error_msg)
                raise Exception(error_msg)
        except Exception as e:
            logger.error(f"Failed to insert data into {table_id}: {str(e)}")
            raise

    def remove_table(self, table_name: string):
        table_id = self.__get_table_id(table_name)
        logger.info(f"Removing table: {table_id}")
        try:
            self.client.delete_table(table_id, not_found_ok=True)
            logger.info(f"Successfully removed table {table_id}")
        except Exception as e:
            logger.error(f"Failed to remove table {table_id}: {str(e)}")
            raise

    def __get_table_id(self, table_name: string) -> string:
        project = os.getenv('GCP_PROJECT')
        dataset = os.getenv('DATASET')
        return f"{project}.{dataset}.{table_name}"
