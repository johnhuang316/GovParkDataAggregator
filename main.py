import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from api.taipeiapi import TaipeiApi
from process.updateprakinglotprocess import UpdateParkingLotProcess


def main():
    api_list = [TaipeiApi()]
    repository = ParkingLotPepository(BigQueryStorage())
    action = os.getenv("ACTION", default="")
    match  action:
        case "update_parking_lot":
            process = UpdateParkingLotProcess(repository, api_list)
        case _:
            print("not matched")

    process.exec()


if __name__ == "__main__":
    load_dotenv()
    main()
