from .models import EmployeeModel
from .serializers import EmployeeModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class EmployeeListCreate(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeModelSerializer


class EmployeeRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeModelSerializer
