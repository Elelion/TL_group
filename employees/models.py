from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='sub_departments',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.ForeignKey(
        Department,
        related_name='employees',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
