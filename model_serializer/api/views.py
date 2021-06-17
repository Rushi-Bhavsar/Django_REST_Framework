from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from .models import EmployeeModel
from .serializers import EmployeeModelSerializer
import io
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeApi(View):
    def get(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id', None)
        if id is not None:
            employee_model_object = EmployeeModel.objects.get(id=id)
            employee_model_serializer_object = EmployeeModelSerializer(employee_model_object)
            return JsonResponse(employee_model_serializer_object.data)
        employee_model_object = EmployeeModel.objects.all()
        employee_model_serializer_object = EmployeeModelSerializer(employee_model_object, many=True)
        return JsonResponse(employee_model_serializer_object.data, safe=False)

    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        employee_model_serializer_object = EmployeeModelSerializer(data=python_dictionary)
        if employee_model_serializer_object.is_valid():
            employee_model_serializer_object.save()
            return JsonResponse({'msg': 'Employee entry added'})
        return JsonResponse(employee_model_serializer_object.errors)

    def put(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id', None)
        if id is not None:
            employee_model_object = EmployeeModel.objects.get(id=id)
            employee_model_serializer_object = EmployeeModelSerializer(employee_model_object,
                                                                       data=python_dictionary, partial=True)
            if employee_model_serializer_object.is_valid():
                employee_model_serializer_object.save()
                return JsonResponse({'msg': 'Employee Data Updated'})
            return JsonResponse(employee_model_serializer_object.errors)
        return JsonResponse({'msg': 'Employee Data update failed.'})

    def delete(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id', None)
        if id is not None:
            employee_model_object = EmployeeModel.objects.get(id=id)
            employee_model_object.delete()
            return JsonResponse({'msg': 'Employee data deleted'})
        return JsonResponse({'msg': 'Employee Data deletion failed'})
