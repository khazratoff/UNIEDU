from xmlrpc.client import TRANSPORT_ERROR
from rest_framework.response import Response
from rest_framework.decorators import api_view
from courses.models import Courses
from api.serializers import courseSerializer
@api_view(['GET'])
def GetRoutes(request):
    routes=[
        {'GET':'/api/courses'},
        {'GET':'/api/courses/id'},
        {'POST':'/api/users/token'},
        {'POST':'/api/users/token/refresh'},

    ]
    return Response(routes)

@api_view(['GET'])
def getCourses(request):
    courses=Courses.objects.all()
    serializer=courseSerializer(courses, many=True)
    return  Response(serializer.data)   

@api_view(['GET'])
def getCourse(request,pk):
    course=Courses.objects.get(id=pk)
    serializer=courseSerializer(course, many=False)
    return  Response(serializer.data)  