from django.contrib import admin
from core.models import Department, Employee


class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')


admin.site.register(Department, DepartmentModelAdmin)
admin.site.register(Employee, EmployeeModelAdmin)
