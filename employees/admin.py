from django.contrib import admin
from .models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'hire_date', 'salary', 'department')
    list_filter = ('department',)
    search_fields = ('full_name', 'position')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
