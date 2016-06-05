from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from ToDo.models import *
def generate(request):
    for x in range(1,11):
        a=List(name="List "+str(x),created="2016-06-1")
        a.save()
    for x in range(1,11):
        for y in range(1,6):
            a=Item(list=List.objects.get(id=x),description="Description "+str(y),due_date="2016-06-30",completed=0)
            a.save()
    return HttpResponse("Success")

