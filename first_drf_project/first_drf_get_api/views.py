from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


# Model Object - Single Student Data.
def student_info_selected(request, roll_no):
    # Query set, Complex data type.
    student_model_object = StudentModel.objects.get(id=roll_no)
    # Native Python Data type.
    student_serializer_object = StudentSerializer(student_model_object)
    # json_data = JSONRenderer().render(student_serializer_object.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(student_serializer_object.data)


def student_info_selected_by_roll_no(request):
    student_model_object = StudentModel.objects.all()
    student_serializer_object = StudentSerializer(student_model_object, many=True)
    # json_data = JSONRenderer().render(student_serializer_object.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(student_serializer_object.data, safe=False)
