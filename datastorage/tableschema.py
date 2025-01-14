from abc import ABC, abstractmethod
from dataclasses import dataclass
from google.cloud import bigquery


@dataclass
class TableSchema(ABC):
    table_name: str = ''

    @abstractmethod
    def get_create_table_schema(self):
        pass


@dataclass
class ParkingLot(TableSchema):
    def __post_init__(self):
        self.table_name = "parking_lot"

    def get_create_table_schema(self):
        return [
            bigquery.SchemaField("official_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("description", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("county", "STRING"),
            bigquery.SchemaField("district", "STRING"),
            bigquery.SchemaField("address", "STRING"),
            bigquery.SchemaField("total_parking_spaces",
                                 "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("total_motorcycle_spaces",
                                 "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("total_charging_stations",
                                 "INTEGER", mode="REQUIRED"),
        ]


@dataclass
class TimeParkingAvailability(TableSchema):
    def __post_init__(self):
        self.table_name = "time_parking_availability"

    def get_create_table_schema(self):
        return [
            bigquery.SchemaField("official_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("county", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("remaining_parking_spaces",
                                 "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("remaining_motorcycle_spaces",
                                 "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("remaining_charging_stations",
                                 "INTEGER", mode="REQUIRED"),
            bigquery.SchemaField("time",
                                 "TIMESTAMP", mode="REQUIRED"),
        ]
