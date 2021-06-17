import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_basic_crud_project.settings')
import django
django.setup()
from basic_api.models import StudentModel
from faker import Faker


def populate(n=5):
    fake = Faker()
    for entry in range(n):
        fake_name = fake.name()
        fake_roll_number = fake.random_int(min=1, max=100, step=1)
        fake_city = fake.city()
        student_details_object = StudentModel.objects.get_or_create(name=fake_name, roll=fake_roll_number,
                                                                    city=fake_city)[0]
        student_details_object.save()


populate(5)
