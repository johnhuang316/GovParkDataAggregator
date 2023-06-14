import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from repository.parkingavailabilityrepository import ParkingAvailabilityRepository
from api.taipeiapi import TaipeiApi
from api.taoyuanapi import TaoyuanApi
from api.apifactory import ApiFactory
from process.updateprakinglotprocess import UpdateParkingLotProcess
from process.logparkingavailability import LogParkingAvailability
from process.resetparkingavailability import ResetParkingAvailability


def main():
    api_list = [
        TaipeiApi(),
        TaoyuanApi()
    ]
    action = os.getenv("ACTION", default="")
    match  action:
        case "update_parking_lot":
            repository = ParkingLotPepository(BigQueryStorage())
            process = UpdateParkingLotProcess(repository, api_list)
        case "log_parking_availability":
            repository = ParkingAvailabilityRepository(BigQueryStorage())
            process = LogParkingAvailability(repository, api_list)
        case "single_log_parking_availability":
            api_name = os.getenv("API", default="")
            api_factory = ApiFactory(api_name)
            single_api_list = [
                api_factory.get_api()
            ]
            repository = ParkingAvailabilityRepository(BigQueryStorage())
            process = LogParkingAvailability(repository, single_api_list)
        case "reset_parking_availability":
            repository = ParkingAvailabilityRepository(BigQueryStorage())
            process = ResetParkingAvailability(repository)
        case _:
            print("not matched")
    process.exec()


if __name__ == "__main__":
    load_dotenv()
    main()
