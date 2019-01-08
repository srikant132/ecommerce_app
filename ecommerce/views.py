from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context ={
        "title": "Hello World!"
    }
    return render(request,"home_page.html",context) #we can also rener html directly

def about_page(request):
    context ={
        "title": "aboutpage"
    }
    return render(request,"home_page.html",context) #{} here we pass context here i.e additional information

def contact_page(request):
    context ={
        "title": "contact_page"
    }
    return render(request,"home_page.html",context)
