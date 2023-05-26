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
        table_id = os.getenv("BIGQUERY_ID", default="") + \
            table_schema.table_name
        schema = table_schema.get_create_table_schema()

        table = bigquery.Table(table_id, schema=schema)
        table = self.client.create_table(table)  # Make an API request.
        print(
            f"Created table {table.project}.{table.dataset_id}.{table.table_id}"
        )

    def insert_data(self, table: string, datas: list[ParkingData]):
        table_id = os.getenv("BIGQUERY_ID", default="") + table
        errors = self.client.insert_rows_json(
            table_id, [asdict(data) for data in datas], row_ids=[None] * len(datas)
        )  # Make an API request.

        if not errors:
            print("New rows have been added.")
        else:
            print(f"Encountered errors while inserting rows: {errors}")

    def close(self):
        pass
