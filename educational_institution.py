"""Educational institution."""

from typing import Dict


class EducationalInstitution:
    """Educational institution."""

    __short_name: str
    """Short name."""

    @property
    def short_name(self) -> str:
        """Short name: getter."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value: str) -> None:
        """Short name: setter."""
        self.__short_name = value

    __full_name: str
    """Full name."""

    @property
    def full_name(self) -> str:
        """Full name: getter."""
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str) -> None:
        """Full name: setter."""
        self.__full_name = value

    __director_name: str
    """Director's name."""

    @property
    def director_name(self) -> str:
        """Director's name: getter."""
        return self.__director_name

    @director_name.setter
    def director_name(self, value: str) -> None:
        """Director's name: setter."""
        self.__director_name = value

    __region_code: str
    """Code of the region where the educational institution is located."""

    @property
    def region_code(self) -> str:
        """Region code: getter."""
        return self.__region_code

    @region_code.setter
    def region_code(self, value: str) -> None:
        """Region code: setter."""
        self.__region_code = value

    def __init__(self) -> None:
        """Initialisation."""
        self.short_name = ''
        self.full_name = ''
        self.director_name = ''

    def __repr__(self) -> str:
        """Representation."""
        return f'{self.short_name} ({self.full_name}) [{self.region_code}], {self.director_name}'

    def load_from_parsed_json(self, parsed_json: Dict[str, str]):
        """Load data from JSON parsed to a dictionary."""
        if 'short_name' in parsed_json:
            self.short_name = parsed_json['short_name']
        else:
            raise Exception('Missing required element: short_name')
        if 'full_name' in parsed_json:
            self.full_name = parsed_json['full_name']
        else:
            raise Exception('Missing required element: full_name')
        if 'director_name' in parsed_json:
            self.director_name = parsed_json['director_name']
        else:
            raise Exception('Missing required element: director_name')
        if 'region_code' in parsed_json:
            self.region_code = parsed_json['region_code']
        else:
            raise Exception('Missing required element: region_code')

    def load_from_json_file(self, file_name: str) -> None:
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
