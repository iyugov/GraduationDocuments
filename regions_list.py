"""Regions list."""

from typing import Dict


class RegionsList:
    """List of available regions."""

    __regions: Dict[str, str]
    """List of regions."""

    @property
    def regions(self) -> Dict[str, str]:
        """Regions: getter."""
        return self.__regions

    @regions.setter
    def regions(self, value: Dict[str, str]) -> None:
        """Regions: setter."""
        self.__regions = value

    def __init__(self) -> None:
        """Initialisation."""
        self.regions = dict()

    def __repr__(self) -> str:
        """Representation."""
        return f'{self.regions}'

    def load_from_parsed_json(self, parsed_json: Dict[str, str]):
        """Load data from JSON parsed to a dictionary."""
        self.regions = parsed_json

    def load_from_json_file(self, file_name):
        """Load data from JSON file."""
        from json import load, decoder
        self.__init__()
        try:
            with open(file_name) as f:
                data = load(f)
        except (FileNotFoundError, PermissionError) as exception:
            raise exception
        except decoder.JSONDecodeError:
            raise Exception('Wrong data file format.')
        self.load_from_parsed_json(data)
