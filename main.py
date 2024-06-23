from graduation_batch import StudentsGraduationBatch
from educational_institution import EducationalInstitution
from regions_list import RegionsList

batch = StudentsGraduationBatch()
batch.load_from_json_file('graduation_batch.json')
print(batch)

school = EducationalInstitution()
school.load_from_json_file('educational_institution.json')
print(school)

regions = RegionsList()
regions.load_from_json_file('regions_list.json')
print(regions)