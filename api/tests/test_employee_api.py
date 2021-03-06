import pytest
from rest_framework import status
from rest_framework.reverse import reverse

path_employee_list = reverse('employee-list')


@pytest.fixture()
def employee():
    return {
        'name': 'Arnaldo Pereira',
        'email': 'arnaldo@luizalabs.com',
        'department': 'Architecture'
    }


@pytest.fixture()
def expected_employee():
    return {
        'id': 1,
        'name': 'Arnaldo Pereira',
        'email': 'arnaldo@luizalabs.com',
        'department': 'Architecture'
    }


@pytest.mark.django_db
def test_status_code(client):
    response = client.get(path_employee_list)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_employee(create_employee, client, expected_employee):
    response = client.get(path_employee_list)
    assert response.data[0] == expected_employee


@pytest.mark.django_db
def test_post_employee_status_code(client, create_department, employee):
    response = client.post(path_employee_list, employee)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_employee(client, create_department, employee, expected_employee):
    response = client.post(path_employee_list, employee)
    assert response.data == expected_employee


@pytest.mark.django_db
def test_post_employee_without_email_should_return_bad_request(client, create_department, employee, expected_employee):
    client.post(path_employee_list, employee)
    employee.pop('email', None)
    response_without_email = client.post(path_employee_list, employee)
    assert response_without_email.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_delete_employee_status_code(client, create_employee, expected_employee):
    path = reverse('employee-detail', args=[expected_employee['id']])
    response = client.delete(path)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_employee(client, create_employee, expected_employee):
    path = reverse('employee-detail', args=[expected_employee['id']])
    response = client.delete(path)
    assert not response.data
