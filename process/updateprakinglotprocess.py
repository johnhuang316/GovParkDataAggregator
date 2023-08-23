import time
from dataclasses import dataclass
from datastorage.bigquerytableschema import ParkingLot
from api.apierror import ApiError
from .iprocess import IProcess


@dataclass
class UpdateParkingLotProcess(IProcess):

    def exec(self) -> bool:
        success = True
        repository = self.repository
        table_schema = ParkingLot()
        repository.remove_table()
        time.sleep(20)
        repository.create_table(table_schema)
        time.sleep(20)
        for api in self.api_list:
            try:
                print(f"Updating parking lot : {api.api_name}")
                datas = api.get_parking_lot_data()
                print(f"datas.count : {len(datas)}")
                repository.insert_data(datas)
            except ApiError as ex:
                print(f"Failed to update parking lot : {str(ex)}")
                success = False
        return success
