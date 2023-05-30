import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datastorage.bigquerytableschema import TableSchema
from dto.parkingdata import ParkingData


@dataclass
class IDataStorage(ABC):
    @abstractmethod
    def create_table(self, table_schema: TableSchema):
        pass

    @abstractmethod
    def insert_data(self, table_name: string, datas: list[ParkingData]):
        pass

    @abstractmethod
    def remove_table(self, table_name: string):
        pass
