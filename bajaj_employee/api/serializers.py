from rest_framework import serializers
from .models import EmployeeModel, EmployeePunchInModel, EmployeePunchOutModel


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class EmployeePunchInModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePunchInModel
        fields = '__all__'

    def validate_punch_in(self, time_data):
        if 10 > time_data.hour < 19:
            raise serializers.ValidationError('Punch In Time should be between 10:00AM and 20:00PM')
        return time_data


class EmployeePunchOutModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeePunchOutModel
        fields = '__all__'

    def validate_punch_out(self, time_data):
        if 10 > time_data.hour < 19:
            raise serializers.ValidationError('Punch Out Time should be between 10:00AM and 20:00PM')
        return time_data
