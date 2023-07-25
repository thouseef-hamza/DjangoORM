from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Book,Phone
from ormapp.models import Student
# Create your views here.
"""
def Home(request):
     employees=Employee.objects.all().select_related('department') # Employee details + department table details that related in employeee table foreign key
     for employee in employees:
          print(employee.department.name)  #joining in database and return only used in foreign key and one to one field
     return None
"""
# Prefetch Related
def Home(request):
     # books = Book.objects.all()
     # for book in books:
     #      print(book.store_set.all())
     # return None
     books = Book.objects.all().prefetch_related('store_set') # Many to Many Field
     for book in books:
          print(book.store_set.all())          # joining in python and return # here all relationship works
          
# One To One
"""
def my_view(request):
     user_phone = Student.objects.get(id=5).phone.phone_number # Because of One to One We Can Take Phone Object
     print(user_phone)
     
     user = Phone.objects.get(id=1).student.phone_number # Reverse
     print(user,",============================)")
"""
# 1 How to model one to one relationships?

