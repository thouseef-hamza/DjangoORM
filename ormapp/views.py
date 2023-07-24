from django.shortcuts import render

# Create your views here.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Chapter 1   Querying And Filtering

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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
# 5  How to do union of two querysets from same or different models?
""" 
<> In this query it will work, if the table have not same number of column it will not union---------------------->
q1 = Student.objects.filter(id__lte=2)
q2 = Student.objects.filter(id__gte=3) 
q2.union(q1)

<> if the table have no same number of column!
Student.objects.all().values('email').union(StudentProfile.objects.all().values('first_name'))
                                                 |
values() ==> + Returns Dictionaries              |   values_list()==> + Returns Tuples
             + can handle additional operations  |                   + Does Not Support Opperations
               (e.g., filtering, aggregations)   |
                                                 |
"""
# 6  How to select some fields only in a queryset?
"""
q1 = Student.objects.filter(email__istartswith='t').values('email','phone_number') 
<> Output will be list of dictonaries -----------------------------------------------> 
 
q1 = Student.objects.filter(email__istartswith = 't').only('email')
<> Output wiil be list of tuples ---------------------------------------------------->

q1 = MyModel.objects.values_list('field1', 'field2')
<> The only difference between 'only' and 'values' is 'only' also fetches the id.---->
"""

# 7 How to do a subquery expression in Django?

"""
------------------------------------------------------------------->
from django.db.models import Subquery
q1 = Student.objects.all()
StudentProfile.objects.filter(user_id__in=Subquery(q1.values('id')))    
-------------------------------------------------------------------->
from django.db.models import Subquery,OuterRef
hero_qs = Hero.objects.filter(
category=OuterRef("pk")
).order_by("-benevolence_factor")
CategoryHero.objects.all().annotate( 
   most_benevolent_hero=Subquery(
       hero_qs.values('name')[:1]
   )
)
"""

# 8  How to filter a queryset with criteria based on comparing their field values

"""
<<<<>>>>    F is For Comparing

<> first_name==last_name
from django.db.models import F
StudentProfile.objects.filter(last_name=F("first_name"))

<> First Name And Last Name Starts With Same First Letter
from django.db.models.functions import Substr
StudentProfile.objects.annotate(first=Substr("first_name", 1, 1), last=Substr("last_name",1,1)).filter(first = F("last"))
"""

# 9  How to filter FileField without any file?
"""
no_files_objects = MyModel.objects.filter(Q(file='')|Q(file=None))

"""

# 10  How to perform join operations in django ORM?
"""
<> One To One Gield Only For select_related()
a1 = Student.objects.select_related('studentprofile') 
"""

# 11 How to find second largest record using Django ORM ?
"""
q1 = Course.objects.order_by("-end_date")[1]
q1.instructor

<<<>>>  first(), last()  <<<>>>>
q1 = Course.objects.first()
q1 = Course.objects.last()
"""

# 12 Find rows which have duplicate field values
"""
duplicates = People.objects.values(
    'first_name'
).annotate(name_count=Count('first_name')).filter(name_count__gt=1)
----------------------------------------------------------------------------------->
records = People.objects.filter(first_name__in=[item['first_name'] for item in 
duplicates])
[item.id for item in records] 
[3, 12, 14] showing the id for the 3 duplicates
""" 

# 13 How to find distinct field values from queryset?
"""
records = People.objects.values(  
   'first_name'
).annotate(
   name_count = Count('first_name')
).filter(name_count=1)
"""

# 14 How to group records in Django ORM?
"""
Using Aggregate Functions------------------->
People.objects.all().aggregate(Avg('id'))
People.objects.all().aggregate(Max('id'))
People.objects.all().aggregate(Min('id'))
People.objects.all().aggregate(Sum('id'))
"""

# 17 How to use arbitrary database functions in querysets? Func provides using arbitary(Lower,Coalesce,Max)
"""
from django.db.models import Func, F
Hero.objects.annotate(like_zeus=Func(F('name'), function='levenshtein', template="
%(function)s(%(expressions)s, 'Zeus')"))

class LevenshteinLikeZeus(Func):
    function='levenshtein'
    template="%(function)s(%(expressions)s, 'Zeus')"
"""

# =========================================================================================================================
# ========================================== Ordering Things ==============================================================
# =========================================================================================================================

# 1 How to order a queryset in ascending or descending order?
#  Ascending ======>
"""
Course.objects.all().order_by('created_at') 
"""
# Descending ========>
"""
Course.objects.all().order_by('-created_at') 
"""
# 2 How to order a queryset in case insensitive manner?
"""
from django.db.models.functions import Lower
StudentProfile.objects.annotate(uname=Lower('first_name')).order_by('uname').values_list('first_name', flat=True)  
"""

# 4 How to order on a field from a related model (with a foreign key)?
"""
Course.objects.all().order_by('category__category_name','title')

Using the double undertscore, you can order on a field
from a related model.
"""

# 5 How to order on an annotated field?
"""
from django.db.models import Count
Course.objects.annotate(hero_count=Count('category')).order_by('-hero_count') 
"""
