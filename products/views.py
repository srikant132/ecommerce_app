# from django.views import ListView                    #This is error we can not import in this way
# from django.views.generic import ListView            #we can also import in this way
from django.views.generic.list import ListView         #impoting ListView from django views
from django.shortcuts import render


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
