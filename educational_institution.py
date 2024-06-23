"""Educational institution."""


class EducationalInstitution:
    """Educational institution."""

    __short_name: str

    @property
    def short_name(self) -> str:
        """Short name: getter."""
        return self.__short_name

    @short_name.setter
    def short_name(self, value) -> None:
        """Short name: setter."""
        self.__short_name = value

    __full_name: str

    @property
    def full_name(self) -> str:
        """Full name: getter."""
        return self.__full_name

    @full_name.setter
    def full_name(self, value) -> None:
        """Full name: setter."""
        self.__full_name = value

    __director_name: str

    @property
    def director_name(self) -> str:
        """Director's name: getter."""
        return self.__director_name

    @director_name.setter
    def director_name(self, value) -> None:
        """Director's name: setter."""
        self.__director_name = value

    __region_code: str

    @property
    def region_code(self) -> str:
        """Region code: getter."""
        return self.__region_code

    @region_code.setter
    def region_code(self, value) -> None:
        """Region code: setter."""
        self.__region_code = value

    def __init__(self) -> None:
        """Initialisation."""
        self.__short_name = ''
        self.__full_name = ''
        self.__director_name = ''

    def __repr__(self) -> str:
        """Representation."""
        return f'{self.short_name} ({self.full_name}) [{self.region_code}], {self.director_name}'

    def load_from_json_file(self, file_name: str) -> None:
        """Load data from JSON file."""
        from json import load, decoder
        self.__short_name = ''
        self.__full_name = ''
        self.__director_name = ''
        try:
            with open(file_name) as f:
                data = load(f)
        except (FileNotFoundError, PermissionError) as exception:
            raise exception
        except decoder.JSONDecodeError:
            raise Exception('Wrong data file format.')
        if 'short_name' in data:
            self.__short_name = data['short_name']
        else:
            raise Exception('Missing required element: short_name')
        if 'full_name' in data:
            self.__full_name = data['full_name']
        else:
            raise Exception('Missing required element: full_name')
        if 'director_name' in data:
            self.__director_name = data['director_name']
        else:
            raise Exception('Missing required element: director_name')
        if 'region_code' in data:
            self.__region_code = data['region_code']
        else:
            raise Exception('Missing required element: region_code')