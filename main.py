import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from repository.parkingavailabilityrepository import ParkingAvailabilityRepository
from api.apifactory import ApiFactory
from process.updateprakinglotprocess import UpdateParkingLotProcess
from process.logparkingavailability import LogParkingAvailability
from process.resetparkingavailability import ResetParkingAvailability


def main():
    api_factory = ApiFactory()
    api_list = [
        api_factory.get_api("Taipei"),
        api_factory.get_api("Taoyuan"),
        api_factory.get_api("NewTaipei"),
    ]
    storage = BigQueryStorage()
    action = os.getenv("ACTION", default="")
    match  action:
        case "update_parking_lot":
            repository = ParkingLotPepository(storage)
            process = UpdateParkingLotProcess(repository, api_list)
        case "log_parking_availability":
            repository = ParkingAvailabilityRepository(storage)
            process = LogParkingAvailability(repository, api_list)
        case "single_log_parking_availability":
            api_name = os.getenv("API", default="")
            single_api_list = [
                api_factory.get_api(api_name)
            ]
            repository = ParkingAvailabilityRepository(storage)
            process = LogParkingAvailability(repository, single_api_list)
        case "reset_parking_availability":
            repository = ParkingAvailabilityRepository(storage)
            process = ResetParkingAvailability(repository)
        case _:
            raise ValueError("no action")

    success = process.exec()
    if not success:
        raise RuntimeError("process failed")


if __name__ == "__main__":
    load_dotenv()
    main()
