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
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))  #here it going to print the data in terminal after submitting

    return render(request,"contact/view.html",context)
