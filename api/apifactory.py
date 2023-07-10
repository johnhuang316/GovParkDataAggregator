import inspect
import sys
from api.iapi import IApi

class ApiFactory:
    def __init__(self):
        self.api_classes = self._find_subclasses(IApi)

    def _find_subclasses(self, cls):
        subclasses = {}
        for _, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj) and issubclass(obj, cls) and obj is not cls:
                api_instance = obj()
                subclasses[api_instance.name] = obj
        return subclasses

    def get_api(self, api_type: str) -> IApi:
        if api_type in self.api_classes:
            return self.api_classes[api_type]()

        raise ValueError(f"The API type '{api_type}' is not supported.")
