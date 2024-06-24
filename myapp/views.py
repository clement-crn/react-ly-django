from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test
from .serializers import MyModelSerializer,TestSerializer
from rest_framework import viewsets

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'je viens de django!'})


@api_view(['GET'])
def get_data(request):
    data = Test.objects.all()
    serializer = MyModelSerializer(data, many=True)
    return Response(serializer.data)


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer