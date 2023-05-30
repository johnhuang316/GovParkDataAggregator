from dataclasses import dataclass
from dto.parkingdata import ParkingData
from datastorage.bigquerytableschema import TableSchema
from .irepository import IPepository


@dataclass
class ParkingAvailabilityRepository(IPepository):
    def __post_init__(self):
        self.table_name = "time_parking_availability"

    def create_table(self, table_schema: TableSchema):
        self.database.create_table(table_schema)

    def insert_data(self, datas: list[ParkingData]):
        self.database.insert_data(self.table_name, datas)

    def remove_table(self):
        self.database.remove_table(self.table_name)
