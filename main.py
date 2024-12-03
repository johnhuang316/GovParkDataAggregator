import os
from dotenv import load_dotenv
from datastorage.bigquerystorage import BigQueryStorage
from repository.parkinglotrepository import ParkingLotPepository
from repository.parkingavailabilityrepository import ParkingAvailabilityRepository
from api.apifactory import ApiFactory
from process.updateprakinglotprocess import UpdateParkingLotProcess
from process.logparkingavailability import LogParkingAvailability
from process.resetparkingavailability import ResetParkingAvailability
from utils.logger import logger

def main():
    logger.info("Starting GovParkDataAggregator")
    api_factory = ApiFactory()
    api_list = [
        api_factory.get_api("Taipei"),
        api_factory.get_api("Taoyuan"),
        api_factory.get_api("NewTaipei"),
    ]
    logger.debug(f"Initialized APIs: {[api.__class__.__name__ for api in api_list]}")
    
    storage = BigQueryStorage()
    action = os.getenv("ACTION", default="")
    logger.info(f"Executing action: {action}")
    
    try:
        match action:
            case "update_parking_lot":
                repository = ParkingLotPepository(storage)
                process = UpdateParkingLotProcess(repository, api_list)
            case "log_parking_availability":
                repository = ParkingAvailabilityRepository(storage)
                process = LogParkingAvailability(repository, api_list)
            case "single_log_parking_availability":
                api_name = os.getenv("API", default="")
                logger.info(f"Processing single API: {api_name}")
                single_api_list = [
                    api_factory.get_api(api_name)
                ]
                repository = ParkingAvailabilityRepository(storage)
                process = LogParkingAvailability(repository, single_api_list)
            case "reset_parking_availability":
                repository = ParkingAvailabilityRepository(storage)
                process = ResetParkingAvailability(repository)
            case _:
                logger.error(f"Invalid action specified: {action}")
                raise ValueError("no action")

        success = process.exec()
        if not success:
            logger.error("Process execution failed")
            raise RuntimeError("process failed")
        logger.info("Process completed successfully")
        
    except Exception as e:
        logger.exception(f"An error occurred during execution: {str(e)}")
        raise

if __name__ == "__main__":
    load_dotenv()
    main()
