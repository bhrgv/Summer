from django.contrib import admin

# Register your models here.
from models import College,Student,Marks

admin.site.register(College)
admin.site.register(Student)
admin.site.register(Marks)

