from django.contrib import admin
from .models import Student,Introduce

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone_number', 'address')

class IntroduceAdmin(admin.ModelAdmin):
	list_display = ('comment')

admin.site.register(Introduce)
admin.site.register(Student)