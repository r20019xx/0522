from django.shortcuts import render_to_response
# Create your views here.
from .models import Student, Introduce

def index(request):
	students = Student.objects.all()
	return render_to_response('cms/menu.html',locals())