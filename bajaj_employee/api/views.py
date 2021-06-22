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


# class EmployeeDetailsAPI(ModelViewSet):
#
# def get_queryset(self, pk=None): if pk is not None: query = "select e.name, e.emp_id, SEC_TO_TIME(sum(
# timestampdiff(second, ed.punch_in, ed.punch_out))) as " \ "'Total Working Hours' from api_employeeloginmodel ed
# inner join api_employeemodel e on " \ "ed.emp_id_id = e.emp_id group by ed.emp_id_id, e.name having e.emp_id = pk;
# " return EmployeeDetailsModel.objects.raw(query) query = "select e.name, e.emp_id, SEC_TO_TIME(sum(timestampdiff(
# second, ed.punch_in, ed.punch_out))) as " \ "'Total Working Hours' from api_employeeloginmodel ed inner join
# api_employeemodel e on ed.emp_id_id " \ "= e.emp_id group by ed.emp_id_id, e.name; " return
# EmployeeDetailsModel.objects.raw(query)
#
#     serializer_class = EmployeeDetailsSerializer


def data():
    emp_detail_list = []
    emp_login_details = EmployeeLoginModel.objects.filter()
    for item in emp_login_details:
        temp_time = lambda time_obj: datetime.datetime.combine(datetime.date(1, 1, 1), time_obj)
        temp_time_diff = temp_time(item.punch_out) - temp_time(item.punch_in)
        emp_detail_list.append({'emp_id': item.employee.emp_id, 'working_hour': temp_time_diff, 'name': item.employee.name})
    return emp_detail_list


def populate_data(emp_details_list):
    for item in emp_details_list:
        employee_object = EmployeeDetailsModel.objects.create(emp_name=item['name'],
                                                                              emp_id=item['emp_id'],
                                                                              working_hours=item['working_hour'])
        employee_object.save()


class EmployeeDetailsAPI(ModelViewSet):
    populate_data(data())
    queryset = EmployeeDetailsModel.objects.all()
    serializer_class = EmployeeDetailsSerializer
