from .models import EmployeeModel
from .serializers import EmployeeModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class EmployeeAPI(ModelViewSet):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()

# class EmployeeAPI(ReadOnlyModelViewSet):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = EmployeeModelSerializer
