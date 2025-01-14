import inspect
import importlib
from pathlib import Path
from .iapi import IApi

class ApiFactory:
    """
    ApiFactory is responsible for dynamically loading and managing API classes.
    
    It scans the 'cities' directory for all Python files, imports the modules,
    and identifies classes that are subclasses of IApi. These classes are then
    stored in a dictionary for easy retrieval based on the API name.
    """
    def __init__(self):
        self.api_classes = self._find_subclasses(IApi)

    def _find_subclasses(self, cls):
        subclasses = {}
        # Get the directory of the cities package
        api_dir = Path(__file__).parent / 'cities'
        
        # Scan for all Python files in the directory
        for file in api_dir.glob("*.py"):
            if file.name.startswith("__"):
                continue
                
            # Convert file path to module name
            module_name = f"api.cities.{file.stem}"
            try:
                # Import the module
                module = importlib.import_module(module_name)
                # Look for classes in the module
                for _, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                        issubclass(obj, cls) and
                        obj is not cls):
                        subclasses[obj.api_name.lower()] = obj
            except ImportError as e:
                print(f"Error importing {module_name}: {e}")
        return subclasses

    def get_api(self, api_name):
        api_class = self.api_classes.get(api_name.lower())
        if not api_class:
            raise ValueError(f"The API type '{api_name}' is not supported.")
        return api_class()

    def get_all_apis(self):
        return [api_class() for api_class in self.api_classes.values()]
