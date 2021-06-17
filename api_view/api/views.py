from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import EmployeeModel
from .serializers import EmployeeModelSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def employee_view(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_serializer_object = EmployeeModelSerializer(emp_model_object)
            return Response(emp_model_serializer_object.data)
        emp_model_object = EmployeeModel.objects.all()
        emp_model_serializer_object = EmployeeModelSerializer(emp_model_object, many=True)
        return Response(emp_model_serializer_object.data)

    if request.method == 'POST':
        emp_model_serializer_object = EmployeeModelSerializer(data=request.data)
        if emp_model_serializer_object.is_valid():
            emp_model_serializer_object.save()
            return Response({'msg': 'Employee details added'})
        return Response(emp_model_serializer_object.errors)

    if request.method == 'PUT':
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_serializer_obj = EmployeeModelSerializer(emp_model_object, data=request.data, partial=True)
            if emp_model_serializer_obj.is_valid():
                emp_model_serializer_obj.save()
                return Response({'msg': f'Data updated for id={id}'})
            return Response(emp_model_serializer_obj.errors)
        return Response({'msg': 'No id passed.'})

    if request.method == 'DELETE':
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_object.delete()
            return Response({'msg': f'Data deleted for employee with id {id}'})
        return Response({'msg': 'No id passed'})


class EmployeeApi(APIView):
    def get(self, request):
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_serializer_object = EmployeeModelSerializer(emp_model_object)
            return Response(emp_model_serializer_object.data)
        emp_model_object = EmployeeModel.objects.all()
        emp_model_serializer_object = EmployeeModelSerializer(emp_model_object, many=True)
        return Response(emp_model_serializer_object.data)

    def post(self, request):
        emp_model_serializer_object = EmployeeModelSerializer(data=request.data)
        if emp_model_serializer_object.is_valid():
            emp_model_serializer_object.save()
            return Response({'msg': 'Employee details added'}, status=status.HTTP_201_CREATED)
        return Response(emp_model_serializer_object.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_serializer_obj = EmployeeModelSerializer(emp_model_object, data=request.data, partial=True)
            if emp_model_serializer_obj.is_valid():
                emp_model_serializer_obj.save()
                return Response({'msg': f'Data updated for id={id}'}, status=status.HTTP_202_ACCEPTED)
            return Response(emp_model_serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'msg': 'No id passed.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.data.get('id')
        if id is not None:
            emp_model_object = EmployeeModel.objects.get(id=id)
            emp_model_object.delete()
            return Response({'msg': f'Data deleted for employee with id {id}'}, status=status.HTTP_200_OK)
        return Response({'msg': 'No id passed'}, status=status.HTTP_400_BAD_REQUEST)
