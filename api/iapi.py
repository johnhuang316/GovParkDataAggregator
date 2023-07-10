from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import requests
from dto.parkingdata import ParkingData
from .apierror import ApiError


@dataclass
class IApi(ABC):

    @property
    def api_name(self):
        pass

    @abstractmethod
    def get_parking_lot_data(self) -> List[ParkingData]:
        pass

    @abstractmethod
    def get_allavailable_data(self) -> List[ParkingData]:
        pass


def call_api(api):
    try:
        response = requests.get(api, timeout=10)
        print(response.status_code)
    except requests.exceptions.HTTPError as error:
        print(f'The request http error : {str(error)}')
        print(f'response status code : {response.status_code}')
        raise ApiError(error) from error
    except requests.exceptions.Timeout as error:
        print('The request timed out')
        raise ApiError(error) from error

    return response
