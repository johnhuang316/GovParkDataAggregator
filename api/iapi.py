from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
from dto.parkingdata import ParkingData


@dataclass
class IApi(ABC):

    @abstractmethod
    def get_parking_lot_data(self) -> List[ParkingData]:
        pass
