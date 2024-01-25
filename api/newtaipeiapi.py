from typing import List
from datetime import datetime
from dto.parkingdata import ParkingData, ParkingLot, TimeParkingAvailability
from .iapi import IApi, call_api


class NewTaipeiApi(IApi):
    api_name = 'NewTaipei'

    def get_parking_lot_data(self) -> List[ParkingData]:
        result = []
        api = "https://data.ntpc.gov.tw/api/datasets/b1464ef0-9c7c-4a6f-abf7-6bdf32847e68/json?size=1000&page=1"

        response = call_api(api)
        print(response.status_code)
        parks = response.json()
        for park in parks:
            result.append(
                ParkingLot(
                    official_id=park.get('ID'),
                    name=park.get('NAME'),
                    description=f"{park.get('SUMMARY')}\n{park.get('PAYEX')}\n{park.get('SERVICETIME')}",
                    county='NewTaipei',
                    district=park.get('AREA'),
                    address=park.get('ADDRESS'),
                    total_parking_spaces=park.get('TOTALCAR', -9),
                )
            )

        api = "https://data.ntpc.gov.tw/api/datasets/b1464ef0-9c7c-4a6f-abf7-6bdf32847e68/json?size=1000"

        response = call_api(api)
        print(response.status_code)
        parks = response.json()
        for park in parks:
            result.append(
                ParkingLot(
                    official_id=park.get('ID'),
                    name=park.get('NAME'),
                    description=f"{park.get('SUMMARY')}\n{park.get('PAYEX')}\n{park.get('SERVICETIME')}",
                    county='NewTaipei',
                    district=park.get('AREA'),
                    address=park.get('ADDRESS'),
                    total_parking_spaces=park.get('TOTALCAR', -9),
                )
            )

        return list(set(result))

    def get_allavailable_data(self) -> List[ParkingData]:
        result = []
        page = 1
        while True:
            api = f"https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/json?size=100&page={
                page}"
            response = call_api(api)
            parks = response.json()
            if not parks:
                break
            now = datetime.now().isoformat(sep=" ", timespec="seconds")
            for park in parks:
                result.append(
                    TimeParkingAvailability(
                        official_id=park.get('ID'),
                        county='NewTaipei',
                        time=now,
                        remaining_parking_spaces=park.get('AVAILABLECAR', -9),
                        remaining_motorcycle_spaces=-9,
                        remaining_charging_stations=-9,
                    )
                )
            page += 1

        return result
