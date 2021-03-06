from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm       #here  we are importing from forms.py Default django form

def home_page(request):
    # print(request.session.get("first_name","Unknown"))  #getter
    # #request.session['first_name']
    context ={
        "title": "Hello World!",
        "content": "Welcome to Homepage.",

    }
    if request.user.is_authenticated():
        context["premium_content"] =  "this is premium content"
    return render(request,"home_page.html",context) #we can also rener html directly

def about_page(request):
    context ={
        "title": "aboutpage",
        "content":"Welcome to Aboutpage "
    }
    return render(request,"home_page.html",context) #{} here we pass context here i.e additional information

def contact_page(request):
    contact_form = ContactForm(request.POST or None) #here we adding the instance of form with ()
    context ={
        "title": "contact_page",
        "content":"Welcome to contactpage ",
        "form":contact_form

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)  #it hold the data if there is a problem
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))  #here it going to print the data in terminal after submitting

    return render(request,"contact/view.html",context)
