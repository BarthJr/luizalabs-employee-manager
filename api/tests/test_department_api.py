import pytest
from rest_framework import status


@pytest.fixture()
def department():
    return {'name': 'Architecture'}


@pytest.fixture()
def expected_department():
    return {'id': 1, 'name': 'Architecture'}


@pytest.mark.django_db
def test_status_code(client):
    response = client.get('/department/')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_department(create_department, client, expected_department):
    response = client.get('/department/')
    assert response.data[0] == expected_department


@pytest.mark.django_db
def test_post_department_status_code(client, department):
    response = client.post('/department/', department)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_post_department(client, department, expected_department):
    response = client.post('/department/', department)
    assert response.data == expected_department


@pytest.mark.django_db
def test_delete_department_status_code(client, create_department, expected_department):
    response = client.delete(f'/department/{expected_department["id"]}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_delete_department_with_nonexistent_id_should_return_not_found(client, create_department, expected_department):
    response = client.delete(f'/department/{0}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_delete_department(client, create_department, expected_department):
    response = client.delete(f'/department/{expected_department["id"]}/')
    assert not response.data
