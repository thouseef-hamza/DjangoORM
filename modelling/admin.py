from django.contrib import admin
from .models import UserParent,Employee,Department,Book,Store,Phone
# Register your models here.

admin.site.register(UserParent)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Phone)