from abc import ABC, abstractmethod
from dataclasses import dataclass
from repository.irepository import IPepository
from api.taipeiapi import IApi


@dataclass
class IProcess(ABC):
    repository: IPepository
    api_list: list[IApi] = None

    @abstractmethod
    def exec(self) -> bool:
        pass
