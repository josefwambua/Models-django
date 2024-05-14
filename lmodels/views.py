from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def home(request):
    obj = Student.objects.all()
    # querying sql
    # print(obj.query)
    # filtering
   # obj = Student.objects.filter(city ="England ")
# Exclude
    #obj = Student.objects.exclude(city = "England")
    obj = Student.objects.order_by('id')
    obj = Student.objects.order_by('?')
    return render(request, 'home.html',{'obj':obj})