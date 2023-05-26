import requests
from typing import List
from dto.parkingdata import ParkingData
from .iapi import IApi


class TaipeiApi(IApi):

    def get_parking_lot_data(self) -> List[ParkingData]:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        print(response.status_code)
        print(response.json())
        return 
