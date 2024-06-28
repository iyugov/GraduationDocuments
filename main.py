from graduation_batch import StudentsGraduationBatch
from educational_institution import EducationalInstitution
from personal_document_template import PersonalDocumentTemplate
from document_generator import DocumentGenerator

generator = DocumentGenerator()

generator.educational_institution = EducationalInstitution()
generator.educational_institution.load_from_json_file('educational_institution.json')

generator.graduation_batch = StudentsGraduationBatch()
generator.graduation_batch.load_from_json_file('graduation_batch.json')

generator.personal_document_template = PersonalDocumentTemplate()
generator.personal_document_template.load_from_json_file('personal_document_template.json')

generator.generate_documents()
