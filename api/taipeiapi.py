from typing import List
from datetime import datetime
import requests
from dto.parkingdata import ParkingData, ParkingLot, TimeParkingAvailability
from .iapi import IApi


class TaipeiApi(IApi):

    def get_parking_lot_data(self) -> List[ParkingData]:
        result = []
        api="https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_alldesc.json"
        try:
            response = requests.get(api, timeout=10)
            print(response.status_code)
            data = response.json()['data']
            print(data['UPDATETIME'])
            parks = data['park']
            for park in parks:
                result.append(
                    ParkingLot(
                        official_id=park.get('id'),
                        name=park.get('name'),
                        description=f"{park.get('summary')}\n{park.get('payex')}",
                        county='Taipei',
                        district=park.get('area'),
                        address=park.get('address'),
                        total_parking_spaces=park.get('totalcar', -9),
                        total_motorcycle_spaces=park.get('totalmotor', -9),
                        total_charging_stations=self.__get_charging_station(
                            park.get('ChargingStation', "").strip())
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
        api = "https://tcgbusfs.blob.core.windows.net/blobtcmsv/TCMSV_allavailable.json"
        try:
            response = requests.get(api, timeout=10)
            print(response.status_code)
            data = response.json()['data']
            print(data['UPDATETIME'])
            parks = data['park']
            now = datetime.now().isoformat(sep=" ", timespec="seconds")
            for park in parks:
                charge_station = park.get('ChargeStation',{"scoketStatusList":[]})
                result.append(
                    TimeParkingAvailability(
                        official_id=park.get('id'),
                        county='Taipei',
                        time=now,
                        remaining_parking_spaces=park.get('availablecar',-9),
                        remaining_motorcycle_spaces=park.get('availablemotor',-9),
                        remaining_charging_stations=self.__abailable_charging(charge_station),
                    )
                )
        except requests.exceptions.HTTPError:
            print('The request http error')
            print(response.status_code)
        except requests.exceptions.Timeout:
            print('The request timed out')
            print(response.status_code)
        return result


    def __get_charging_station(self, value) -> int:
        return -9 if value == "" else int(value)

    def __abailable_charging(self, charge_station) -> int:
        scoket_status_list = charge_station['scoketStatusList']
        if scoket_status_list == []:
            return -9
        return sum(p['spot_status'] == "待機中" for p in scoket_status_list)
