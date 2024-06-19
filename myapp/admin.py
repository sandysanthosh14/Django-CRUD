from django.contrib import admin
from myapp.models import Student

# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list=['name','sub','sclass']

admin.site.register(Student,Studentadmin)