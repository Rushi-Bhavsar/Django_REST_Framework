from rest_framework import serializers
from .models import EmployeeModel


class EmployeeModelSerializer(serializers.ModelSerializer):

    def start_with_r(self, value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with small r only.')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = EmployeeModel
        fields = '__all__'

    def validate_emp_id(self, attrs):
        if attrs > 100:
            raise serializers.ValidationError('Employee ID full')
        return attrs

    def validate(self, attrs):
        obj_name = attrs.get('name')
        obj_city = attrs.get('city')
        if obj_name.lower() == 'rushi bhavsar' and obj_city.lower() != 'nashik':
            raise serializers.ValidationError(f"City must be nashik for employee {obj_name}.")
        return attrs
