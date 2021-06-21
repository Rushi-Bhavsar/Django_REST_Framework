from rest_framework import serializers
from .models import EmployeeModel


class EmployeeModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = '__all__'

