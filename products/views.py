# from django.views import ListView                    #This is error we can not import in this way
# from django.views.generic import ListView            #we can also import in this
#impoting ListView from django views
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404

from .models import Product           #importing model from models
# Create your views here.
#Class Based View
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
#every single classBased view has his method it gets the context for any given queryset or view
    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context


#function Based View
def product_list_view(request):
    queryset = Product.objects.all()          #it allowed to take the data from db
    context = {
        'object_list' : queryset
    }

    return render (request,"products/list.html",context)



class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
 #every single classBased view has his method it gets the context for any given queryset or view
    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        # context['abc'] =123
        return context


#function Based View
def product_detail_view(request,pk=None,*args,**kwargs):
    # instance = Product.objects.get(pk=pk)  #id
    instance = get_object_or_404(Product,pk=pk)
    context = {
        'object' : instance
    }
    return render (request,"products/detail.html",context)
