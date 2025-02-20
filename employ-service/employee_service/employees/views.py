from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
import requests

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        employee = serializer.save()
        
        # Send data to ESB
        esb_url = "http://esb-service-url/employees/"  # Replace with actual ESB endpoint
        data = {
            "id": employee.id,
            "fullname": employee.fullname,
            "dateofbirth": employee.dateofbirth.strftime("%Y-%m-%d"),
            "address": employee.address,
            "contact_number": employee.contact_number,
            "emergency_contact_details": employee.emergency_contact_details
        }
        requests.post(esb_url, json=data)  # Send data to ESB

class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
