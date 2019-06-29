import pytest
from rest_framework.test import APIClient

from core.models import Department, Employee


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def create_department():
    return Department.objects.create(name='Architecture')


@pytest.fixture
def create_employee(create_department):
    employee = {
        'name': 'Arnaldo Pereira',
        'email': 'arnaldo@luizalabs.com',
        'department': create_department
    }
    return Employee.objects.create(**employee)
