"""Graduation batch."""

from datetime import date, datetime
from typing import List, Dict
from student import Student


class StudentsGraduationBatch:
    """Graduation batch."""

    __graduation_year: int
    """Year of graduation."""

    @property
    def graduation_year(self) -> int:
        """Graduation year: getter."""
        return self.__graduation_year

    @graduation_year.setter
    def graduation_year(self, value: int) -> None:
        """Graduation year: setter."""
        if value < 0:
            raise ValueError('Wrong value for graduation year.')
        else:
            self.__graduation_year = value

    __educational_institution_separated_name: List[str]
    """Name of the educational institution separated by lines to fit in documents."""

    @property
    def educational_institution_separated_name(self) -> List[str]:
        """Educational institution separated name: getter."""
        return self.__educational_institution_separated_name

    @educational_institution_separated_name.setter
    def educational_institution_separated_name(self, value: List[str]) -> None:
        """Educational institution separated name: setter."""
        self.__educational_institution_separated_name = value

    __document_issue_date: date
    """Date of issue of documents."""

    @property
    def document_issue_date(self) -> str:
        """Birthdate: getter."""
        return datetime.strftime(self.__document_issue_date, '%d.%m.%Y')

    @document_issue_date.setter
    def document_issue_date(self, value: str) -> None:
        """Birthdate: getter."""
        self.__document_issue_date = datetime.strptime(value, '%d.%m.%Y')

    __educational_institution_signatory_officer_name: str
    """Name of the signatory officer of the educational institution."""

    @property
    def educational_institution_signatory_officer_name(self) -> str:
        """Educational institution signatory officer's name: getter."""
        return self.__educational_institution_signatory_officer_name

    @educational_institution_signatory_officer_name.setter
    def educational_institution_signatory_officer_name(self, value: str) -> None:
        """Educational institution signatory officer's name: setter."""
        self.__educational_institution_signatory_officer_name = value

    __educational_institution_signatory_officer_position: str
    """Position of the signatory officer of the educational institution."""

    @property
    def educational_institution_signatory_officer_position(self) -> str:
        """Educational institution signatory officer's position: getter."""
        return self.__educational_institution_signatory_officer_position

    @educational_institution_signatory_officer_position.setter
    def educational_institution_signatory_officer_position(self, value: str) -> None:
        """Educational institution signatory officer's position: setter."""
        self.__educational_institution_signatory_officer_position = value

    __students_list: List[Student]
    """List of students to receive documents."""

    @property
    def students_list(self) -> List[Student]:
        """Students list: getter."""
        return self.__students_list

    @students_list.setter
    def students_list(self, value: List[Student]) -> None:
        """Students list: setter."""
        self.__students_list = value

    def __init__(self):
        """Initialisation."""
        self.graduation_year = 0
        self.educational_institution_signatory_officer_name = ''
        self.educational_institution_signatory_officer_position = ''
        self.educational_institution_separated_name = []
        self.document_issue_date = '01.01.0001'
        self.students_list = []

    def __repr__(self) -> str:
        """Representation."""
        result = '===\n'
        result += f'{self.graduation_year}\n'
        result += '===\n'
        for name_component in self.educational_institution_separated_name:
            result += f'{name_component}\n'
        result += '===\n'
        if self.educational_institution_signatory_officer_name != '':
            result += f'{self.educational_institution_signatory_officer_name}\n'
        if self.educational_institution_signatory_officer_position != '':
            result += f'{self.educational_institution_signatory_officer_position}\n'
        result += '===\n'
        result += f'{self.document_issue_date}\n'
        result += '===\n'
        for student in self.students_list:
            result += f'{student}\n'
        result += '==='
        return result

    def load_from_parsed_json(self, parsed_json: Dict[str, str | Dict | List[str]]):
        """Load data from JSON parsed to a dictionary."""
        if 'educational_institution_separated_name' in parsed_json:
            self.educational_institution_separated_name = parsed_json['educational_institution_separated_name']
        else:
            raise Exception('Missing required section: educational_institution_separated_name')
        if 'document_issue_date' in parsed_json:
            self.document_issue_date = parsed_json['document_issue_date']
        else:
            raise Exception('Missing required element: document_issue_date')
        field_name = 'educational_institution_signatory_officer_name'
        if field_name in parsed_json:
            self.educational_institution_signatory_officer_name = parsed_json[field_name]
        field_name = 'educational_institution_signatory_officer_position'
        if field_name in parsed_json:
            self.educational_institution_signatory_officer_position = parsed_json[field_name]
        if 'students' in parsed_json:
            students_data = parsed_json['students']
        else:
            raise Exception('Missing required section: students')
        for student_data in students_data:
            new_student = Student()
            new_student.load_from_parsed_json(student_data)
            self.students_list.append(new_student)

    def load_from_json_file(self, file_name: str):
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
