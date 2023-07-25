from django.db import models
# from django.contrib.auth.models import User
from ormapp.models import Student

# Create your models here.

class UserParent(models.Model):
     user = models.OneToOneField(
          Student,
          on_delete=models.CASCADE,
          primary_key=True,
     )
     father_name = models.CharField(max_length=100)
     mother_name = models.CharField(max_length=100)

class Department(models.Model):
     name = models.CharField(max_length=50)
     
     def __str__(self):
          return self.name

class Employee(models.Model):
     name = models.CharField(max_length=124)
     age = models.IntegerField()
     department = models.ForeignKey(Department,on_delete=models.CASCADE)
     
     def __str__(self):
          return self.name
     
class Book(models.Model):
     name = models.CharField(max_length=308)
     price = models.IntegerField(default=0)
     
     def __str__(self):
          return self.name
     
class Store(models.Model):
     name = models.CharField(max_length=308)
     books = models.ManyToManyField(Book)
     
     def __str__(self):
          return self.name

class Phone(models.Model):
     phone_number = models.CharField(max_length=13)
     student = models.OneToOneField(Student,on_delete=models.CASCADE,related_name='phone')
     