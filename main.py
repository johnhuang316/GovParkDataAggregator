import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from api.apifactory import get_api
from process.updateprakinglotprocess import UpdateParkingLotProcess
from process.logparkingavailability import LogParkingAvailability
from process.resetparkingavailability import ResetParkingAvailability


def main():
    api_list = [
        get_api("Taipei"),
        get_api("Taoyuan")
    ]
    repository = ParkingLotPepository(BigQueryStorage())
    action = os.getenv("ACTION", default="")
    match  action:
        case "update_parking_lot":
            process = UpdateParkingLotProcess(repository, api_list)
        case "log_parking_availability":
            process = LogParkingAvailability(repository, api_list)
        case "single_log_parking_availability":
            api_name = os.getenv("API", default="")
            single_api_list = [
                get_api(api_name)
            ]
            process = LogParkingAvailability(repository, single_api_list)
        case "reset_parking_availability":
            process = ResetParkingAvailability(repository)
        case _:
            raise ValueError("no action")

    successed = process.exec()
    if not successed:
        raise RuntimeError("process failed")


if __name__ == "__main__":
    load_dotenv()
    main()
