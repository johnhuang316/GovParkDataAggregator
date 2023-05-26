from abc import ABC, abstractmethod
from dataclasses import dataclass
from dto.parkingdata import ParkingData
from datastorage.idatastorage import IDataStorage


@dataclass
class IPepository(ABC):
    database:IDataStorage

    @abstractmethod
    def insert_data(self, datas: list[ParkingData]):
        pass
