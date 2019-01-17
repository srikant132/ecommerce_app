from django.shortcuts import render

# Create your views here.
def cart_home(request):
    # print(request.session)  #on the request of sessions
    # print(dir(request.session))
    # request.session.set_expiry(300)   #5 minutes
    #key = request.session.session_key
    #print(key)
    request.session['cart_id'] = 11   #setter
    request.session['user'] = request.user.username
    return render(request,"carts/home.html",{})
