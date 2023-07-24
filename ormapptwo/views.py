from django.shortcuts import render

# Create your views here.


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Chapter 2   Creating,Updating and Deleting things
    
    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1 How to create multiple objects in one shot?
"""
Category.objects.bulk_create(
    [Category(name="Humanities"),
     Category(name="ComputerScience"),
     Category(name="HomeScience")]
  )
"""
# 2 How to copy or clone an existing model object?
"""
Category.objects.all().count()  # ==> 5
q2=Category.objects.last()
q2.pk=None 
q2.save()
Category.objects.all().count() # ==> 6 
"""
# 3 How to ensure that only one object can be created? Page 24
# 4 How to update denormalized fields in other models on save? Page 25

# 5 How to perform truncate like operation using Django ORM? Page 26 for truncate method 
"""
Category.objects.all().delete()
"""
# 6 What signals are raised by Django during object creation or update? Page 26 for more
"""
• pre_init
• post_init
• pre_save
• post_save
• pre_delete
• post_delete
"""

# 7