import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_view.settings')
import django
django.setup()
from api.models import EmployeeModel
from faker import Faker


def populate(n=5):
    fake = Faker()
    for entry in range(n):
        fake_name = fake.name()
        fake_emp_id = fake.random_int(min=1, max=100, step=1)
        fake_city = fake.city()
        student_details_object = EmployeeModel.objects.get_or_create(name=fake_name, emp_id=fake_emp_id,
                                                                    city=fake_city)[0]
        student_details_object.save()


populate(5)
