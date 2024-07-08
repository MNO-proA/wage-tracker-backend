from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from .models import WorkHour
from .serializers import WorkHourSerializer
from rest_framework import viewsets
from .models import EmployeeAbsence
from .serializers import EmployeeAbsenceSerializer

class WorkHourListCreateView(generics.ListCreateAPIView):
    queryset = WorkHour.objects.all().order_by('-shift_start')
    serializer_class = WorkHourSerializer
    permission_classes=[]

    @swagger_auto_schema(operation_description="Retrieve a list of work hours")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new work hour")
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WorkHourRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkHour.objects.all()
    serializer_class = WorkHourSerializer
    permission_classes=[]

    @swagger_auto_schema(operation_description="Retrieve a specific work hour")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific work hour")
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific work hour")
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class EmployeeAbsenceViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAbsence.objects.all()
    serializer_class = EmployeeAbsenceSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save()
        
    def perform_update(self, serializer):
        serializer.save()