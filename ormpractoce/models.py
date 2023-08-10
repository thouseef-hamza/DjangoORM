from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Teacher(models.Model):
     teacher_name = models.CharField(max_length=255)
     
     
     def __str__(self) -> str:
          return self.teacher_name
     
     

class Course(models.Model):
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True)
    course_name = models.CharField(max_length=125)
    price = models.IntegerField()
    
    def __str__(self) -> str:
         return self.course_name
    
class Lesson(models.Model):
     course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True)
     lesson_name = models.CharField(max_length=125)
     
     def __str__(self) -> str:
          return self.lesson_name

class Chapter(models.Model):
     lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=True)
     chapter_name = models.CharField(max_length=125)
     index_no = models.IntegerField()
     
     def __str__(self) -> str:
          return self.chapter_name