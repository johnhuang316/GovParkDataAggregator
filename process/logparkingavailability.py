from dataclasses import dataclass
from .iprocess import IProcess


@dataclass
class LogParkingAvailability(IProcess):

    def exec(self):
        repository = self.repository
        for api in self.api_list:
            datas = api.get_allavailable_data()
            repository.insert_data(datas)
