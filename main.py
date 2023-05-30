import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from repository.parkingavailabilityrepository import ParkingAvailabilityRepository
from api.taipeiapi import TaipeiApi
from process.updateprakinglotprocess import UpdateParkingLotProcess
from process.logparkingavailability import LogParkingAvailability
from process.resetparkingavailability import ResetParkingAvailability


def main():
    api_list = [TaipeiApi()]
    action = os.getenv("ACTION", default="")
    match  action:
        case "update_parking_lot":
            repository = ParkingLotPepository(BigQueryStorage())
            process = UpdateParkingLotProcess(repository, api_list)
        case "log_parking_availability":
            repository = ParkingAvailabilityRepository(BigQueryStorage())
            process = LogParkingAvailability(repository, api_list)
        case "reset_parking_availability":
            repository = ParkingAvailabilityRepository(BigQueryStorage())
            process = ResetParkingAvailability(repository)
        case _:
            print("not matched")

    process.exec()


if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("ACTION"))
    print(os.getenv("BIGQUERY_ID"))
    main()
