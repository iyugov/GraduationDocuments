"""Personal document template."""

from decimal import Decimal
from typing import Dict


class PersonalDocumentTemplate:
    """Personal document template."""

    __title: str
    """Title of the document (one side)."""

    @property
    def title(self) -> str:
        """Title: getter."""
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """Title: setter."""
        self.__title = value

    __blank_width: Decimal
    """Blank width, mm."""

    @property
    def blank_width(self) -> Decimal:
        """Blank width: getter."""
        return self.__blank_width

    @blank_width.setter
    def blank_width(self, value: Decimal) -> None:
        """Blank width: setter."""
        self.__blank_width = value

    __blank_height: Decimal
    """Blank height, mm."""

    @property
    def blank_height(self) -> Decimal:
        """Blank height: getter."""
        return self.__blank_height

    @blank_height.setter
    def blank_height(self, value: Decimal) -> None:
        """Blank height: setter."""
        self.__blank_height = value

    def __init__(self) -> None:
        """Initialisation."""
        self.title = ''
        self.blank_width = Decimal(0)
        self.blank_height = Decimal(0)

    def __repr__(self) -> str:
        """Representation."""
        return f'"{self.title}", {self.blank_width}x{self.blank_height}'

    def load_from_parsed_json(self, parsed_json: Dict[str, str | Decimal]):
        """Load data from JSON parsed to a dictionary."""
        if 'title' in parsed_json:
            self.title = parsed_json['title']
        else:
            raise Exception('Missing required element: title')
        if 'blank_width' in parsed_json:
            self.blank_width = Decimal(parsed_json['blank_width'])
        else:
            raise Exception('Missing required element: blank_width')
        if 'blank_height' in parsed_json:
            self.blank_height = Decimal(parsed_json['blank_height'])
        else:
            raise Exception('Missing required element: blank_height')

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
