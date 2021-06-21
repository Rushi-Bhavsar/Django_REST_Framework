from .models import EmployeeModel, EmployeePunchInModel, EmployeePunchOutModel
from .serializers import EmployeeModelSerializer, EmployeePunchInModelSerializer, EmployeePunchOutModelSerializer
from rest_framework.viewsets import ModelViewSet


class EmployeeAPI(ModelViewSet):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()


class EmployeePunchInAPI(ModelViewSet):
    serializer_class = EmployeePunchInModelSerializer
    queryset = EmployeePunchInModel.objects.all()


class EmployeePunchOutAPI(ModelViewSet):
    serializer_class = EmployeePunchOutModelSerializer
    queryset = EmployeePunchOutModel.objects.all()


