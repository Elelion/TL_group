import os
import django
import random
from faker import Faker

# указываем переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Dj_TL_group_TZ.settings')
django.setup()

# Теперь импортируем модели после установки настроек
from employees.models import Department, Employee

fake = Faker()


# **


def create_departments():
    departments = []

    level1 = [Department(name=f"Department Level 1 - {i}") for i in range(5)]
    Department.objects.bulk_create(level1)
    level1 = Department.objects.all()
    departments.extend(level1)

    level2 = [Department(name=f"Department Level 2 - {i}", parent=random.choice(level1)) for i in range(5)]
    Department.objects.bulk_create(level2)
    level2 = Department.objects.filter(parent__in=level1)
    departments.extend(level2)

    level3 = [Department(name=f"Department Level 3 - {i}", parent=random.choice(level2)) for i in range(5)]
    Department.objects.bulk_create(level3)
    level3 = Department.objects.filter(parent__in=level2)
    departments.extend(level3)

    level4 = [Department(name=f"Department Level 4 - {i}", parent=random.choice(level3)) for i in range(5)]
    Department.objects.bulk_create(level4)
    level4 = Department.objects.filter(parent__in=level3)
    departments.extend(level4)

    level5 = [Department(name=f"Department Level 5 - {i}", parent=random.choice(level4)) for i in range(5)]
    Department.objects.bulk_create(level5)
    level5 = Department.objects.filter(parent__in=level4)
    departments.extend(level5)

    return departments


def create_employees(departments):
    employees = []
    for _ in range(50000):
        department = random.choice(departments)
        employee = Employee(
            full_name=fake.name(),
            position=fake.job(),
            hire_date=fake.date_this_decade(),
            salary=random.randint(30000, 150000),
            department=department
        )
        employees.append(employee)
    Employee.objects.bulk_create(employees)


if __name__ == "__main__":
    Department.objects.all().delete()
    Employee.objects.all().delete()
    departments = create_departments()
    create_employees(departments)
    print("Database populated successfully!")
