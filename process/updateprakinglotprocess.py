import time
from dataclasses import dataclass
from datastorage.bigquerytableschema import ParkingLot
from .iprocess import IProcess


@dataclass
class UpdateParkingLotProcess(IProcess):

    def exec(self):
        repository = self.repository
        table_schema = ParkingLot()
        repository.remove_table()
        repository.create_table(table_schema)
        time.sleep(20)
        for api in self.api_list:
            datas = api.get_parking_lot_data()
            repository.insert_data(datas)
