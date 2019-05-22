from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	address = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name

class Introduce(models.Model):
	#name = models.CharField(max_length=20)
	#age = models.DecimalField(max_digits=100, decimal_places=0)
	comment = models.CharField(max_length=50)
	#sex = models.BooleanField(default=False)
	student = models.ForeignKey('Student',on_delete=models.CASCADE)


	def __str__(self):
		return self.comment