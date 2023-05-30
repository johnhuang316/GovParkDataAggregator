import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from dto.parkingdata import ParkingData
from datastorage.idatastorage import IDataStorage
from datastorage.bigquerytableschema import TableSchema


@dataclass
class IPepository(ABC):
    database: IDataStorage
    table_name: string = ''

    @abstractmethod
    def create_table(self, table_schema: TableSchema):
        pass

    @abstractmethod
    def insert_data(self, datas: list[ParkingData]):
        pass

    @abstractmethod
    def remove_table(self):
        pass
