from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from customers.models import customer
from rest_framework import status
from django.http import Http404
from .serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated



@permission_classes((IsAuthenticated,))
class CustomerList(APIView):
    def get(self,request):
        customers = customer.objects.all()
        serializer = CustomerSerializer(customers,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@permission_classes((IsAuthenticated,))
class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return customer.objects.get(pk=pk)
        except customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)