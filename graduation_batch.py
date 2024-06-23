"""Graduation batch."""

from typing import List

from student import Student


class StudentsGraduationBatch:

    __educational_institution_separated_name: List[str]

    __educational_institution_signatory_officer_name: str

    __educational_institution_signatory_officer_position: str

    __students_list: List[Student]

    def __init__(self):
        """Initialisation."""
        self.__educational_institution_separated_name = []
        self.__students_list = []

    def __repr__(self) -> str:
        """Representation."""
        result = '===\n'
        for name_component in self.__educational_institution_separated_name:
            result += f'{name_component}\n'
        result += '===\n'
        if self.__educational_institution_signatory_officer_name != '':
            result += f'{self.__educational_institution_signatory_officer_name}\n'
        if self.__educational_institution_signatory_officer_position != '':
            result += f'{self.__educational_institution_signatory_officer_position}\n'
        result += '===\n'
        for student in self.__students_list:
            result += f'{student}\n'
        result += '==='
        return result

    def load_from_json_file(self, file_name):
        """Load data from JSON file."""
        from json import load, decoder
        self.__students_list = []
        self.__educational_institution_separated_name = []
        self.__educational_institution_signatory_officer_name = ''
        self.__educational_institution_signatory_officer_position = ''
        try:
            with open(file_name) as f:
                data = load(f)
        except (FileNotFoundError, PermissionError) as exception:
            raise exception
        except decoder.JSONDecodeError:
            raise Exception('Wrong data file format.')
        if 'educational_institution_separated_name' in data:
            self.__educational_institution_separated_name = data['educational_institution_separated_name']
        else:
            raise Exception('Missing required section: educational_institution_separated_name')
        field_name = 'educational_institution_signatory_officer_name'
        if field_name in data:
            self.__educational_institution_signatory_officer_name = data[field_name]
        field_name = 'educational_institution_signatory_officer_position'
        if field_name in data:
            self.__educational_institution_signatory_officer_position = data[field_name]
        if 'students' in data:
            students_data = data['students']
        else:
            raise Exception('Missing required section: students')
        for student_data in students_data.values():
            new_student = Student()
            if 'last_name' in student_data:
                new_student.last_name = student_data['last_name']
            else:
                self.__students_list = []
                raise Exception('Missing required element: last_name')
            if 'first_name' in student_data:
                new_student.first_name = student_data['first_name']
            else:
                self.__students_list = []
                raise Exception('Missing required element: first_name')
            if 'patronymic' in student_data:
                new_student.patronymic = student_data['patronymic']
            else:
                self.__students_list = []
                raise Exception('Missing required element: patronymic (however, it can be empty)')
            self.__students_list.append(new_student)
