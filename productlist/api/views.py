from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
# to create teh below funciton as an API, we're using @api_view
@api_view()
def getData(request):
    return Response({"message":"Hello Akhil"})
