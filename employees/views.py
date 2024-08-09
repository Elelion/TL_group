from django.shortcuts import render
from .models import Department


def department_tree(request):
    departments = Department.objects.all()

    context = {
        'departments': departments
    }

    return render(request, 'employees/department_tree.html', context)
