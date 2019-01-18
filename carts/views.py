from django.shortcuts import render,redirect

from products.models import Product
from .models import Cart

# Create your views here.
def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request,"carts/home.html",{"cart":cart_obj})

#here we creating views for the cart
def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id =product_id)

        except Product.DoesNotExists:
            print("Show message to user, product is gone?")
            return redirect("cart:home")

        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)

        else:
            cart_obj.products.add(product_obj)

        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")