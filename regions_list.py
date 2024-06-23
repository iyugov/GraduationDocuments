"""Regions list."""

from typing import Dict


class RegionsList:
    __regions: Dict[str, str]

    def __init__(self) -> None:
        """Initialisation."""
        self.__regions = dict()

    def __repr__(self) -> str:
        """Representation."""
        return f'{self.__regions}'

    def load_from_json_file(self, file_name):
        """Load data from JSON file."""
        from json import load, decoder
        self.__regions = dict()
        try:
            with open(file_name) as f:
                data = load(f)
        except (FileNotFoundError, PermissionError) as exception:
            raise exception
        except decoder.JSONDecodeError:
            raise Exception('Wrong data file format.')
        self.__regions = data
