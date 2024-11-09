from django.shortcuts import render


from rest_framework.response import Response 
from rest_framework.decorator import api_view

@api_view(['GET'])
def getData(request):
    return Response({"message": "Hello" })