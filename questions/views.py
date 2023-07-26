from django.shortcuts import render

# Create your views here.

# 1 What Is Django ORM ?
"""
<> A feature that allows to interact with database using python objects
<> we can define our database schema using Python classes, 
   and the ORM takes care of translating those classes into the corresponding database tables and columns.
==> Key Features :-
               <> Models :- Python Class represents DB table , class attributes corresponds column of a table
               <> Fields :- determine the datatype and constraints corresponding db columns
               <> Querysets :- A collection of database queries
               <> Migrations :- Migration system that automatically handles datbase changes without loosing data
               <> Relations :- make relationship between models. 
"""

# 2 What are the advantages of using Django ORM?
"""
<> Portabilty :- we can develop application using one database ,for production we can switch to another
<> Django MVT Architecture :- seperation for model part enhances code maintainabilty and readabilty to handles fb operaions.
<> 
"""