from .models import EmployeeModel
from .serializers import EmployeeModelSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, \
    RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class EmployeeAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GetByIdEmployeeAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = EmployeeModelSerializer
    queryset = EmployeeModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
