import inspect
import pkgutil
import api
from .iapi import IApi


class ApiFactory:
    def __init__(self):
        self.api_classes = self._find_subclasses(IApi)

    def _find_subclasses(self, cls):
        subclasses = {}
        # Import every module in the 'api' package
        for _, name, _ in pkgutil.walk_packages(api.__path__, api.__name__ + '.'):
            module = __import__(name, fromlist='dummy')
            for _, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, cls) and obj is not cls:
                    subclasses[obj.api_name] = obj
        return subclasses

    def get_api(self, api_type: str) -> IApi:
        if api_type in self.api_classes:
            return self.api_classes[api_type]()

        raise ValueError(f"The API type '{api_type}' is not supported.")
