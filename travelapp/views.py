from django.shortcuts import render
from django.http import HttpResponse
from . models import place
from . models import blog
def fun(request):
    obj=place.objects.all
    obj1=blog.objects.all
    return render(request,'index.html',{'results':obj,"News":obj1})


def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,'result.html',{'sum':num3})
