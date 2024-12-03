import inspect
import importlib
import os
from pathlib import Path
from .iapi import IApi


class ApiFactory:
    def __init__(self):
        self.api_classes = self._find_subclasses(IApi)

    def _find_subclasses(self, cls):
        subclasses = {}
        # Get the directory of the api package
        api_dir = Path(__file__).parent
        
        # Scan for all Python files in the directory
        for file in api_dir.glob("*.py"):
            if file.name.startswith("__"):
                continue
                
            # Convert file path to module name
            module_name = f"api.{file.stem}"
            try:
                # Import the module
                module = importlib.import_module(module_name)
                # Look for classes in the module
                for _, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, cls) and 
                        obj is not cls and 
                        hasattr(obj, 'api_name')):
                        subclasses[obj.api_name] = obj
            except ImportError as e:
                print(f"Failed to import {module_name}: {e}")
                
        return subclasses

    def get_api(self, api_type: str) -> IApi:
        if api_type in self.api_classes:
            return self.api_classes[api_type]()

        raise ValueError(f"The API type '{api_type}' is not supported.")
