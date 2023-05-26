import string
from abc import ABC, abstractmethod
from dataclasses import dataclass
from dto.parkingdata import ParkingData

@dataclass
class IQueryFactory(ABC):

    @abstractmethod
    def get_insert_string(self, data:ParkingData) -> string:
        pass
    