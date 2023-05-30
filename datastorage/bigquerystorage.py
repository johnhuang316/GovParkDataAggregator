import os
import string
from dataclasses import asdict, dataclass
from google.cloud import bigquery
from dto.parkingdata import ParkingData
from .idatastorage import IDataStorage
from .bigquerytableschema import TableSchema


@dataclass
class BigQueryStorage(IDataStorage):
    client: bigquery.Client = None

    def __post_init__(self):
        self.client = bigquery.Client()

    def create_table(self, table_schema: TableSchema):
        table_id = self.__get_table_id(table_schema.table_name)
        schema = table_schema.get_create_table_schema()

        table = bigquery.Table(table_id, schema=schema)
        table = self.client.create_table(table)
        print(
            f"Created table {table.project}.{table.dataset_id}.{table.table_id}"
        )

    def insert_data(self, table_name: string, datas: list[ParkingData]):
        table_id = self.__get_table_id(table_name)
        errors = self.client.insert_rows_json(table_id, [asdict(data) for data in datas], row_ids=[None] * len(datas))
        if not errors:
            print("New rows have been added.")
        else:
            print(f"Encountered errors while inserting rows: {errors}")

    def remove_table(self, table_name: string):
        table_id = self.__get_table_id(table_name)
        self.client.delete_table(table_id, not_found_ok=True)
        print(f"Deleted table '{table_id}")

    def __get_table_id(self, table_name: string) -> string:
        dataset_id = os.getenv("BIGQUERY_ID", default="")
        table_id = f"{dataset_id}.{table_name}"
        print(table_id)
        return table_id
