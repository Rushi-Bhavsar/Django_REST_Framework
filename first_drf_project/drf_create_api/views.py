import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def student_create(request):
    if request.method == "POST":
        # Store the JSON data from the request body.
        json_data = request.body

        # Convert the JSON data into stream.
        stream = io.BytesIO(json_data)

        # Convert stream into native python data type dictionary.
        python_data = JSONParser().parse(stream)

        # Convert python dictionary into complex data type (model object).
        serializer = StudentSerializer(data=python_data)

        # Check if data stored in serializer is valid data.
        if serializer.is_valid():
            # Saving the data inside the model.
            serializer.save()
            # Sending response that data is stored in the model.
            return JsonResponse({'msg': 'Student entry done.'})
        # In case data is not valid then error message will be returned.
        return JsonResponse(serializer.errors)
