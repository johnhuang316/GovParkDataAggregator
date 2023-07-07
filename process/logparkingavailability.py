from dataclasses import dataclass
from api.apierror import ApiError
from .iprocess import IProcess


@dataclass
class LogParkingAvailability(IProcess):
    def exec(self) -> bool:
        repository = self.repository
        result = True
        for api in self.api_list:
            try:
                datas = api.get_allavailable_data()
                repository.insert_data(datas)
            except ApiError as ex:
                print(f"Failed to call : {str(ex)}")
                result = False

        return result
