# luizalabs-employee-manager
[![Build Status](https://travis-ci.com/BarthJr/luizalabs-employee-manager.svg?branch=master)](https://travis-ci.com/BarthJr/luizalabs-employee-manager)
[![Updates](https://pyup.io/repos/github/BarthJr/luizalabs-employee-manager/shield.svg)](https://pyup.io/repos/github/BarthJr/luizalabs-employee-manager/)
[![Python 3](https://pyup.io/repos/github/BarthJr/luizalabs-employee-manager/python-3-shield.svg)](https://pyup.io/repos/github/BarthJr/luizalabs-employee-manager/)

The goal is to create a Django Admin panel and an API to manage employees.

## Application available in Heroku
**Applications**|**URL**
:--|:--
Django Admin panel|https://luizalabs-test-barthjr.herokuapp.com/admin/
API|https://luizalabs-test-barthjr.herokuapp.com/api/v1/


# Installation

1. Clone the repository
2. Change to the directory was created by the clone
3. Install pipenv
4. Activate virtualenv
5. Run application

``` console
git clone https://github.com/BarthJr/luizalabs-employee-manager.git
cd luizalabs-employee-manager
pip install pipenv
pipenv shell
./run.sh
```
# Acess to Admin Panel
- **URL:** http://127.0.0.1:8000/admin/
- **Username:** luiza.labs
- **Password:** clubedalulu


# Endpoints RESTful
- **Base URL:** http://127.0.0.1:8000/api/v1
## Department
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
GET|/department|Returns all departments
GET|/department/{id}|Returns department by id
POST|/department|Creates department
PUT|/department/{id}|Updates department
DELETE|/department/{id}|Deletes department by id

## Employee
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
GET|/employee|Returns all employees
GET|/employee/{id}|Returns employee by id
POST|/employee|Creates employee
PUT|/employee/{id}|Updates employee
DELETE|/employee/{id}|Deletes employee by id

# API Examples
## Create Department
```console
curl -X POST http://127.0.0.1:8000/api/v1/department/ -d "name=TI"
```
## Create Employee
```console
curl -X POST http://127.0.0.1:8000/api/v1/employee/ -d "name=Junior Barth&email=junior.barth@luizalabs.com&department=TI"
```

## Update Employee
```console
curl -X PUT http://127.0.0.1:8000/api/v1/employee/1/ -d "name=Barth&email=junior.barth@luizalabs.com&department=TI"
```

## Get Department
```console
curl http://127.0.0.1:8000/api/v1/department/
```
- Response
```console
[
  {
    "id":1,
    "name":"TI"
  }
]
```
## Delete Department
```console
curl -X DELETE http://127.0.0.1:8000/api/v1/department/1/
```

