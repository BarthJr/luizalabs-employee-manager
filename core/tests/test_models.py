import pytest
from core.models import Department, Employee


@pytest.fixture
def department():
    return Department.objects.create(name='Architecture')


@pytest.fixture
def employee(department):
    employee = {
        'name': 'Arnaldo Pereira',
        'email': 'arnaldo@luizalabs.com',
        'department': department
    }
    return Employee.objects.create(**employee)


@pytest.mark.django_db
def test_create_department(department):
    assert Department.objects.exists()


@pytest.mark.django_db
def test_create_employee(employee):
    assert Employee.objects.exists()
