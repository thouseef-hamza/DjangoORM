from django.shortcuts import render

# Create your views here.

# 1  How to find the query associated with a queryset?
"""
queryset = Chapter.objects.all()
str(queryset.query)
'SELECT "ormapp_chapter"."id", "ormapp_chapter"."course_id", "ormapp_chapter"."title", "ormapp_chapter"."order", "ormapp_chapter"."created_at", "ormapp_chapter"."updated_at" FROM "ormapp_chapter"' 
"""

# 2  How to do OR queries in Django ORM?
"""
from django.db.models import Q     
qs = Student.objects.filter(Q(email__istartswith='t')|Q(email__istartswith='s'))
"""

# 3  How to do AND queries in Django ORM?
"""
from django.db.models import Q     
qs = Student.objects.filter(Q(email__istartswith='t') & Q(email__iendswith='.com'))
"""

# 4  How to do a NOT query in Django queryset
                    #---------------Method 1 --------------------
""" 
from django.db.models import Q
qs = Student.objects.filter(~Q(email__istartswith="t"))
"""
                    #---------------Method 2 --------------------
"""
qs = Student.objects.exclude(email__istartswith="t")  
"""
            
# 5  How to select some fields only in a queryset?
"""
q1 = Student.objects.filter(email__istartswith='t').values('email','phone_number') 
<> Output will be list of dictonaries ----------------------------------------------->  
q1 = Student.objects.filter(email__istartswith = 't').only('email')
<> Output wiil be list of tuples ---------------------------------------------------->
q1 = MyModel.objects.values_list('field1', 'field2')
<> The only difference between 'only' and 'values' is 'only' also fetches the id.---->
"""

#6 How to do a subquery expression in Django?

"""
from django.db.models import Subquery
q1 = Student.objects.all()
StudentProfile.objects.filter(user_id__in=Subquery(q1.values('id')))    
<QuerySet [<StudentProfile: StudentProfile object (1)>, <StudentProfile: StudentProfile object (2)>, <StudentProfile: StudentProfile object (3)>, <StudentProfile: StudentProfile object (4)>]>
"""