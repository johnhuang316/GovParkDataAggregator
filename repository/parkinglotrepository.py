import string
from dataclasses import dataclass
from dto.parkingdata import ParkingData
from datastorage.bigquerytableschema import TableSchema
from .irepository import IPepository


@dataclass
class ParkingLotPepository(IPepository):

    def create_table(self, table_schema: TableSchema):
        self.database.create_table(table_schema)

    def insert_data(self, datas: list[ParkingData]):
        self.database.insert_data("parking_lot", datas)

    def remove_table(self, table_name: string):
        self.database.remove_table(table_name)
