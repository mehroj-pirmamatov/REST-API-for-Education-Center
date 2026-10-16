from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    role = models.CharField(
        max_length=10, 
        choices=Role.choices, 
        default=Role.ADMIN 
    )
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"



class Teacher(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)
    experience = models.IntegerField()  

    def __str__(self):
        return self.full_name


class Student(models.Model):
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name
    

    






