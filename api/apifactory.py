from dataclasses import dataclass
from api import taipeiapi, taoyuanapi, iapi


@dataclass
class ApiFactory:
    api_name: str

    def get_api(self) -> iapi.IApi:
        match self.api_name:
            case "Taipei":
                api = taipeiapi.TaipeiApi()
            case "Taoyuan":
                api = taoyuanapi.TaoyuanApi()
            case _:
                raise ValueError("no api")
        return api
