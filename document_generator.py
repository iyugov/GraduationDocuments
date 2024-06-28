"""Document generator."""

from personal_document_template import PersonalDocumentTemplate
from graduation_batch import StudentsGraduationBatch
from educational_institution import EducationalInstitution

from qrcode import QRCode, constants
from os import system
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import mm


class DocumentGenerator:
    __educational_institution: EducationalInstitution
    """Educational institution."""

    @property
    def educational_institution(self) -> EducationalInstitution:
        """Educational institution: getter."""
        return self.__educational_institution

    @educational_institution.setter
    def educational_institution(self, value: EducationalInstitution) -> None:
        """Educational institution: setter."""
        self.__educational_institution = value

    __graduation_batch: StudentsGraduationBatch
    """Graduation batch."""

    @property
    def graduation_batch(self) -> StudentsGraduationBatch:
        """Graduation batch: getter."""
        return self.__graduation_batch

    @graduation_batch.setter
    def graduation_batch(self, value: StudentsGraduationBatch) -> None:
        """Graduation batch: setter."""
        self.__graduation_batch = value

    __personal_document_template: PersonalDocumentTemplate
    """Personal document template."""

    @property
    def personal_document_template(self) -> PersonalDocumentTemplate:
        """Personal document template: getter."""
        return self.__personal_document_template

    @personal_document_template.setter
    def personal_document_template(self, value: PersonalDocumentTemplate) -> None:
        """Personal document template: setter."""
        self.__personal_document_template = value

    def __init__(self):
        self.educational_institution = None
        self.graduation_batch = None
        self.personal_document_template = None

    def generate_documents(self) -> None:
        students = self.graduation_batch.students_list
        for student in students:
            print(student)
            qr_code = QRCode(
                version=6,
                error_correction=constants.ERROR_CORRECT_Q,
                box_size=10,
                border=4,
            )
            qr_data_components = [
                student.last_name,
                student.first_name,
                student.patronymic,
                self.educational_institution.region_code,
                '0',
                self.graduation_batch.document_issue_date
            ]
            qr_data = '|'.join(qr_data_components)
            png_file_name = f'{student.social_insurance_number}.png'
            print(qr_data)
            qr_code.add_data(qr_data)
            qr_code.make(fit=True)
            img = qr_code.make_image(fill_color="black", back_color="white")
            img.save(png_file_name)
            pdf_file_name = f'{student.social_insurance_number}.pdf'
            blank_width = float(self.personal_document_template.blank_width)
            blank_height = float(self.personal_document_template.blank_height)
            canvas = Canvas(pdf_file_name, pagesize=(blank_width * mm, blank_height * mm))
            canvas.setFont("Times-Roman", 11)
            canvas.drawInlineImage(png_file_name, 20 * mm, 20 * mm, 20 * mm, 20 * mm)
            canvas.save()
            system(f'open "{pdf_file_name}"')
