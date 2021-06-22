from rest_framework import serializers
from .models import EmployeeModel, EmployeeLoginModel, EmployeeDetailsModel


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class EmployeeLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeLoginModel
        fields = '__all__'

    def validate(self, time_data):
        pin = time_data.get('punch_in')
        pout = time_data.get('punch_out')
        if 10 > pin.hour < 19 and 10 > pout.hour < 19:
            raise serializers.ValidationError('Punch In and Punch Out Time should be between 10:00AM and 20:00PM')
        return time_data


class EmployeeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDetailsModel
        fields = '__all__'

