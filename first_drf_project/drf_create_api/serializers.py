from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    roll_no = serializers.IntegerField()
    city = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)