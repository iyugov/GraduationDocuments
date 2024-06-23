"""Student."""


class Student:

    __last_name: str

    @property
    def last_name(self) -> str:
        """Last name: getter."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value) -> None:
        """Last name: setter."""
        self.__last_name = value

    __first_name: str

    @property
    def first_name(self) -> str:
        """First name: getter."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value) -> None:
        """First name: setter."""
        self.__first_name = value

    __patronym: str

    @property
    def patronymic(self) -> str:
        """Patronymic: getter."""
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value) -> None:
        """Patronymic: setter."""
        self.__patronymic = value

    def __init__(self) -> None:
        """Initialisation."""
        self.__last_name = ''
        self.__first_name = ''
        self.__patronymic = ''

    def __repr__(self) -> str:
        """Representation."""
        result = f'{self.last_name} {self.first_name}'
        if self.patronymic != '':
            result += f' {self.patronymic}'
        return result

    def load_from_json_file(self, file_name: str) -> None:
        """Load data from JSON file."""
        from json import load, decoder
        self.__last_name = ''
        self.__first_name = ''
        self.__patronymic = ''
        try:
            with open(file_name) as f:
                data = load(f)
        except (FileNotFoundError, PermissionError) as exception:
            raise exception
        except decoder.JSONDecodeError:
            raise Exception('Wrong data file format.')
        if 'last_name' in data:
            self.__last_name = data['last_name']
        else:
            raise Exception('Missing required element: last_name')
        if 'first_name' in data:
            self.__first_name = data['first_name']
        else:
            raise Exception('Missing required element: first_name')
        if 'patronymic' in data:
            self.__patronymic = data['patronymic']
        else:
            raise Exception('Missing required element: patronymic (however, it can be empty)')
