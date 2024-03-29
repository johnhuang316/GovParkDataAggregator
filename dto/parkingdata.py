from dataclasses import dataclass
from abc import ABC


@dataclass
class ParkingData(ABC):
    def __post_init__(self):
        pass


@dataclass
class ParkingLot(ParkingData):
    official_id: str
    name: str
    description: str = ""
    county: str = ""
    district: str = ""
    address: str = ""
    total_parking_spaces: int = -9
    total_motorcycle_spaces: int = -9
    total_charging_stations: int = -9

    def __eq__(self, other):
        if not isinstance(other, ParkingLot):
            return False
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


@dataclass
class TimeParkingAvailability(ParkingData):
    official_id: str
    county: str
    time: str
    remaining_parking_spaces: int = -9
    remaining_motorcycle_spaces: int = -9
    remaining_charging_stations: int = -9
