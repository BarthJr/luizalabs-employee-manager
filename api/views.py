from rest_framework import viewsets

from api.serializers import EmployeeSerializer, DepartmentSerializer
from core.models import Employee, Department


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
