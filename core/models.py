from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
