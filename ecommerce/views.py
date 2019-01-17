from django.contrib.auth import authenticate,login,get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect



from .forms import ContactForm,LoginForm,RegisterForm         #here  we are importing from forms.py Default django form

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
#here we are using the forms.py functionality for login_page
def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            "form":form
        }
    print("User logged In")
    print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username =form.cleaned_data.get("username")
        password =form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            login(request,user)
            #redirect to a success page
            #context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error")


    return render(request,"auth/login.html", context)


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            "form":form
        }
    if form.is_valid():
        print(form.cleaned_data)
        username =form.cleaned_data.get("username")
        email =form.cleaned_data.get("email")
        password =form.cleaned_data.get("password")
        new_user = User.objects.create_user(username,email,password)
        print(new_user)
    return render(request,"auth/register.html",context)
