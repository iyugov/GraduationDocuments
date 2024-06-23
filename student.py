"""Student."""

from datetime import date, datetime
from typing import Dict
from enum import Enum
from re import fullmatch


class Gender(Enum):
    """Gender."""
    FEMALE = 'Ж'
    MALE = 'М'


class Student:
    """Student."""

    __last_name: str
    """Last name."""

    @property
    def last_name(self) -> str:
        """Last name: getter."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Last name: setter."""
        self.__last_name = value

    __first_name: str
    """First name."""

    @property
    def first_name(self) -> str:
        """First name: getter."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """First name: setter."""
        self.__first_name = value

    __patronymic: str
    """Patronymic."""

    @property
    def patronymic(self) -> str:
        """Patronymic: getter."""
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str) -> None:
        """Patronymic: setter."""
        self.__patronymic = value

    __birth_date: date
    """Birthdate."""

    @property
    def birth_date(self) -> str:
        """Birthdate: getter."""
        return datetime.strftime(self.__birth_date, '%d.%m.%Y')

    @birth_date.setter
    def birth_date(self, value: str) -> None:
        """Birthdate: getter."""
        self.__birth_date = datetime.strptime(value, '%d.%m.%Y')

    __gender: Gender | None
    """Gender."""

    @property
    def gender(self) -> Gender | None:
        """Gender: getter."""
        return self.__gender

    @gender.setter
    def gender(self, value: Gender | None) -> None:
        """Gender: setter."""
        self.__gender = value

    __social_insurance_number: str | None
    """Social insurance number, a unique identifier."""

    @property
    def social_insurance_number(self) -> str:
        """Social insurance number: getter."""
        if self.__social_insurance_number is None:
            return ''
        else:
            return self.__social_insurance_number

    @social_insurance_number.setter
    def social_insurance_number(self, value: str) -> None:
        """Social insurance number: setter."""
        if self.social_insurance_number_is_correct(value):
            self.__social_insurance_number = value
        else:
            self.__social_insurance_number = None
            raise ValueError('Wrong value for social insurance number.')

    def __init__(self) -> None:
        """Initialisation."""
        self.last_name = ''
        self.first_name = ''
        self.patronymic = ''
        self.birth_date = '01.01.0001'
        self.gender = None
        self.social_insurance_number = None

    def __repr__(self) -> str:
        """Representation."""
        result = f'{self.last_name} {self.first_name}'
        if self.patronymic != '':
            result += f' {self.patronymic}'
        if isinstance(self.gender, Gender):
            result += f' ({self.gender.value})'
        result += f', {self.birth_date}'
        result += f', [{self.social_insurance_number}]'
        return result

    def load_from_parsed_json(self, parsed_json: Dict[str, str]):
        """Load data from JSON parsed to a dictionary."""
        if 'last_name' in parsed_json:
            self.last_name = parsed_json['last_name']
        else:
            raise Exception('Missing required element: last_name')
        if 'first_name' in parsed_json:
            self.first_name = parsed_json['first_name']
        else:
            raise Exception('Missing required element: first_name')
        if 'patronymic' in parsed_json:
            self.patronymic = parsed_json['patronymic']
        else:
            raise Exception('Missing required element: patronymic (however, it can be empty)')
        if 'gender' in parsed_json:
            try:
                self.gender = parsed_json['gender']
            except ValueError:
                raise ValueError('Wrong data element: gender')
        else:
            raise Exception('Missing required element: gender')
        if 'birth_date' in parsed_json:
            self.birth_date = parsed_json['birth_date']
        else:
            raise Exception('Missing required element: birth_date')
        if 'social_insurance_number' in parsed_json:
            try:
                self.social_insurance_number = parsed_json['social_insurance_number']
            except ValueError:
                raise ValueError('Wrong data element: social_insurance_number')
        else:
            raise Exception('Missing required element: social_insurance_number')

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

    @staticmethod
    def social_insurance_number_is_correct(number: str | None) -> bool:
        """Check if social insurance number is empty or correct."""
        if number is None:
            return True
        if not fullmatch('[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9] [0-9][0-9]', number):
            return False
        number = number.replace('-', '').replace(' ', '')
        for digit in '0123456789':
            if digit * 3 in number:
                return False
        control_number = int(number[-2:])
        digits_weighted_sum = sum(int(number[index]) * (9 - index) for index in range(len(number) - 2))
        return digits_weighted_sum % 101 == control_number
