from dataclasses import dataclass
from dto.parkingdata import ParkingData
from datastorage.tableschema import TableSchema
from .irepository import IPepository


@dataclass
class ParkingLotPepository(IPepository):
    def __post_init__(self):
        self.table_name = "parking_lot"

    def create_table(self, table_schema: TableSchema):
        self.database.create_table(table_schema)

    def insert_data(self, datas: list[ParkingData]):
        self.database.insert_data(self.table_name, datas)

    def remove_table(self):
        self.database.remove_table(self.table_name)
