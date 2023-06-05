from typing import List
from datetime import datetime
import requests
from dto.parkingdata import ParkingData, ParkingLot, TimeParkingAvailability
from .iapi import IApi


class TaoyuanApi(IApi):

    def get_parking_lot_data(self) -> List[ParkingData]:
        result = []
        api = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f"
        try:
            response = requests.get(api, timeout=10)
            print(response.status_code)
            data = response.json()
            parks = data['parkingLots']
            for park in parks:
                result.append(
                    ParkingLot(
                        official_id=park.get('parkId'),
                        name=park.get('parkName'),
                        description=f"{park.get('introduction')}\n{park.get('payGuide')}",
                        county='Taoyuan',
                        district=park.get('areaName'),
                        address=park.get('address'),
                        total_parking_spaces=park.get('totalSpace', -9)
                    )
                )
        except requests.exceptions.HTTPError:
            print('The request http error')
            print(response.status_code)
        except requests.exceptions.Timeout:
            print('The request timed out')
            print(response.status_code)

        return result

    def get_allavailable_data(self) -> List[ParkingData]:
        result = []
        api = "https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f"
        try:
            response = requests.get(api, timeout=10)
            print(response.status_code)
            data = response.json()
            parks = data['parkingLots']
            now = datetime.now().isoformat(sep=" ", timespec="seconds")
            for park in parks:
                result.append(
                    TimeParkingAvailability(
                        official_id=park.get('parkId'),
                        county='Taoyuan',
                        time=now,
                        remaining_parking_spaces=int(park.get('surplusSpace', "-9"))
                    )
                )
        except requests.exceptions.HTTPError:
            print('The request http error')
            print(response.status_code)
        except requests.exceptions.Timeout:
            print('The request timed out')
            print(response.status_code)
        return result