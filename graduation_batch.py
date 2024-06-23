"""Graduation batch."""

from typing import List, Dict

from student import Student


class StudentsGraduationBatch:

    __educational_institution_separated_name: List[str]

    @property
    def educational_institution_separated_name(self) -> List[str]:
        """Educational institution separated name: getter."""
        return self.__educational_institution_separated_name

    @educational_institution_separated_name.setter
    def educational_institution_separated_name(self, value: List[str]) -> None:
        """Educational institution separated name: setter."""
        self.__educational_institution_separated_name = value

    __educational_institution_signatory_officer_name: str

    @property
    def educational_institution_signatory_officer_name(self) -> str:
        """Educational institution signatory officer's name: getter."""
        return self.__educational_institution_signatory_officer_name

    @educational_institution_signatory_officer_name.setter
    def educational_institution_signatory_officer_name(self, value: str) -> None:
        """Educational institution signatory officer's name: setter."""
        self.__educational_institution_signatory_officer_name = value

    __educational_institution_signatory_officer_position: str

    @property
    def educational_institution_signatory_officer_position(self) -> str:
        """Educational institution signatory officer's position: getter."""
        return self.__educational_institution_signatory_officer_position

    @educational_institution_signatory_officer_position.setter
    def educational_institution_signatory_officer_position(self, value: str) -> None:
        """Educational institution signatory officer's position: setter."""
        self.__educational_institution_signatory_officer_position = value

    __students_list: List[Student]

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
        self.__educational_institution_separated_name = []
        self.__students_list = []

    def __repr__(self) -> str:
        """Representation."""
        result = '===\n'
        for name_component in self.educational_institution_separated_name:
            result += f'{name_component}\n'
        result += '===\n'
        if self.educational_institution_signatory_officer_name != '':
            result += f'{self.educational_institution_signatory_officer_name}\n'
        if self.educational_institution_signatory_officer_position != '':
            result += f'{self.educational_institution_signatory_officer_position}\n'
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
        for student_data in students_data.values():
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
