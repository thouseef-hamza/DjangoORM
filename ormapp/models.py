from django.db import models

# Create User models here.

class Student(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.email

class StudentProfile(models.Model):
    user = models.OneToOneField(Student,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    address = models.TextField()

    
class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
     
class Instructor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
class People(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.username
    
class CategoryHero(models.Model):
    name = models.CharField(max_length=100)
    
class Hero(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(CategoryHero, on_delete=models.CASCADE)
    benevolence_factor = models.PositiveSmallIntegerField(
    help_text="How benevolent this hero is?",
    default=50
    )
    
