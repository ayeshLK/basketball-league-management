from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def hello_world(request):
    """
    Hello world API in this project. This is used to test whether the configurations work.
    """
    return Response({"message": "Hello, world!"})     
