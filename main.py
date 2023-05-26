from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from dto.parkingdata import ParkingLot
from repository.parkinglotrepository import ParkingLotPepository
from api.taipeiapi import TaipeiApi


def main():
    api = TaipeiApi()
    api.get_parking_lot_data()
    # repository = ParkingLotPepository(BigQueryStorage())
    # repository.insert_data(datas)



if __name__ == "__main__":
    load_dotenv()
    main()
