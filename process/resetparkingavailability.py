from dataclasses import dataclass
from datastorage.bigquerytableschema import TimeParkingAvailability
from .iprocess import IProcess


@dataclass
class ResetParkingAvailability(IProcess):

    def exec(self):
        repository = self.repository
        table_schema = TimeParkingAvailability()
        repository.remove_table()
        repository.create_table(table_schema)
