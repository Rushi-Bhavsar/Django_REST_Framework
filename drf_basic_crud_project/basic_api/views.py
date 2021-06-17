import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from .models import StudentModel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator


# Function based view.
@csrf_exempt
def student_info(request, roll_no=None):
    if request.method == 'GET':
        # json_data = request.body
        # if json_data is None:
        #     print("None")
        # print(json_data)
        # print(type(json_data))
        # stream = io.BytesIO(json_data)
        # print(type(stream))
        # python_dictionary = JSONParser().parse(stream)
        # id = python_dictionary.get('id', None)
        if roll_no is not None:
            student_model_object = StudentModel.objects.get(id=roll_no)
            student_serializer_object = StudentSerializer(student_model_object)
            return JsonResponse(student_serializer_object.data)
        student_model_object = StudentModel.objects.all()
        student_serializer_object = StudentSerializer(student_model_object, many=True)
        return JsonResponse(student_serializer_object.data, safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        student_serializer_object = StudentSerializer(data=python_dictionary)
        if student_serializer_object.is_valid():
            student_serializer_object.save()
            return JsonResponse({'msg': 'Student entry done.'})
        return JsonResponse(student_serializer_object.errors)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id')
        student_model_object = StudentModel.objects.get(id=id)
        student_serializer_object = StudentSerializer(student_model_object, data=python_dictionary, partial=True)
        # student_serializer_object = StudentSerializer(student_model_object, data=python_dictionary)
        if student_serializer_object.is_valid():
            student_serializer_object.save()
            return JsonResponse({'msg': 'Data Updated successfully'})
        return JsonResponse(student_serializer_object.errors)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id')
        student_model_object = StudentModel.objects.get(id=id)
        student_model_object.delete()
        return JsonResponse({'msg': 'Student record deleted.'})


# Class base view.
@method_decorator(csrf_exempt, name='dispatch')
class StudentView(View):
    def get(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id', None)
        if id is not None:
            student_model_object = StudentModel.objects.get(id=id)
            student_serializer_object = StudentSerializer(student_model_object)
            return JsonResponse(student_serializer_object.data)
        student_model_object = StudentModel.objects.all()
        student_serializer_object = StudentSerializer(student_model_object, many=True)
        return JsonResponse(student_serializer_object.data, safe=False)

    def post(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        student_serializer_object = StudentSerializer(data=python_dictionary)
        if student_serializer_object.is_valid():
            student_serializer_object.save()
            return JsonResponse({'msg': 'Student entry done.'})
        return JsonResponse(student_serializer_object.errors)

    def put(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id')
        student_model_object = StudentModel.objects.get(id=id)
        student_serializer_object = StudentSerializer(student_model_object, data=python_dictionary, partial=True)
        # student_serializer_object = StudentSerializer(student_model_object, data=python_dictionary)
        if student_serializer_object.is_valid():
            student_serializer_object.save()
            return JsonResponse({'msg': 'Data Updated successfully'})
        return JsonResponse(student_serializer_object.errors)

    def delete(self, request):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_dictionary = JSONParser().parse(stream)
        id = python_dictionary.get('id')
        student_model_object = StudentModel.objects.get(id=id)
        student_model_object.delete()
        return JsonResponse({'msg': 'Student record deleted.'})