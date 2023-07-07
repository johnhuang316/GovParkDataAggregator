import time
from dataclasses import dataclass
from datastorage.bigquerytableschema import ParkingLot
from api.apierror import ApiError
from .iprocess import IProcess


@dataclass
class UpdateParkingLotProcess(IProcess):

    def exec(self) -> bool:
        try:
            repository = self.repository
            table_schema = ParkingLot()
            repository.remove_table()
            repository.create_table(table_schema)
            time.sleep(20)
            for api in self.api_list:
                datas = api.get_parking_lot_data()
                repository.insert_data(datas)
            return True
        except ApiError as ex:
            print(f"Failed to update parking lot : {str(ex)}")
            return False
