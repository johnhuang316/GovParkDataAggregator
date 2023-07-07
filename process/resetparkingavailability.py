from dataclasses import dataclass
from datastorage.bigquerytableschema import TimeParkingAvailability
from api.apierror import ApiError
from .iprocess import IProcess



@dataclass
class ResetParkingAvailability(IProcess):

    def exec(self) -> bool:
        try:
            repository = self.repository
            table_schema = TimeParkingAvailability()
            repository.remove_table()
            repository.create_table(table_schema)
            return True
        except ApiError as ex:
            print(f"Failed to reset parking availability : {str(ex)}")
            return False
