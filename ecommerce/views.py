from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context ={
        "title": "Hello World!",
        "content": "Welcome to Homepage."
    }
    return render(request,"home_page.html",context) #we can also rener html directly

def about_page(request):
    context ={
        "title": "aboutpage",
        "content":"Welcome to Aboutpage "
    }
    return render(request,"home_page.html",context) #{} here we pass context here i.e additional information

def contact_page(request):
    context ={
        "title": "contact_page",
        "content":"Welcome to contactpage "
    }
    return render(request,"home_page.html",context)
