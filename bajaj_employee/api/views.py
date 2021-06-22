import datetime
from .models import EmployeeModel, EmployeeLoginModel, EmployeeDetailsModel
from .serializers import EmployeeModelSerializer, EmployeeLoginSerializer, EmployeeDetailsSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class EmployeeAPI(ModelViewSet):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()


class EmployeeLoginAPI(ModelViewSet):
    serializer_class = EmployeeLoginSerializer
    queryset = EmployeeLoginModel.objects.all()


def data():
    emp_detail_list = []
    for employee in EmployeeModel.objects.all():
        emp_login_details = EmployeeLoginModel.objects.filter(employee=employee)
        total_time = datetime.timedelta()
        for item in emp_login_details:
            temp_time = lambda time_obj: datetime.datetime.combine(datetime.date(1, 1, 1), time_obj)
            temp_time_diff = temp_time(item.punch_out) - temp_time(item.punch_in)
            total_time = total_time + temp_time_diff
        emp_detail_list.append({'emp_id': employee.emp_id, 'working_hour': str(total_time), 'name': employee.name})
    return emp_detail_list


def populate_data(emp_details_list):
    for item in emp_details_list:
        EmployeeDetailsModel.objects.get_or_create(emp_name=item['name'],
                                                   emp_id=item['emp_id'],
                                                   working_hours=item['working_hour'])


class EmployeeDetailsAPI(ReadOnlyModelViewSet):
    populate_data(data())
    lookup_field = 'emp_id'
    queryset = EmployeeDetailsModel.objects.all()
    serializer_class = EmployeeDetailsSerializer
