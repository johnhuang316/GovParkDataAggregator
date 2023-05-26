from dataclasses import dataclass
from dto.parkingdata import ParkingData
from .irepository import IPepository


@dataclass
class ParkingLotPepository(IPepository):

    def insert_data(self, datas: list[ParkingData]):
        self.database.insert_data("parking_lot", datas)
