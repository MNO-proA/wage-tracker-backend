from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []
    
    @swagger_auto_schema(operation_description="Retrieve a list of employees")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new employee")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @swagger_auto_schema(operation_description="Retrieve a specific employee")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific employee")
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific employee")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)