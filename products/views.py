# from django.views import ListView                    #This is error we can not import in this way
# from django.views.generic import ListView            #we can also import in this
#impoting ListView from django views
from  django.http import Http404
from django.views.generic import ListView,DetailView
from django.shortcuts import render,get_object_or_404

#importing model from models
from .models import Product

# Create your views here.
#Class Based View

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
         request = self.request
         return  Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    template_name = Product.objects.all().featured()

    # def get_queryset(self,*args,**kwargs):
    #      request = self.request
    #      return  Product.objects.featured()



class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/list.html"
    #every single classBased view has his method it gets the context for any given queryset or view

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs)
    #     print(context)
    #     return context
    def get_queryset(self,*args,**kwargs):
         request = self.request
         return  Product.objects.all()


#function Based View
def product_list_view(request):
    queryset = Product.objects.all()          #it allowed to take the data from db
    context = {
        'object_list' : queryset
    }

    return render (request,"products/list.html",context)


class  ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"


class ProductDetailView(DetailView):
     # queryset = Product.objects.all()
    template_name = "products/detail.html"
 #every single classBased view has his method it gets the context for any given queryset or view

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        # context['abc'] =123
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instace


     # def get_queryset(self,*args,**kwargs):
     #     request = self.request
     #     pk = self.kwargs.get('pk')
     #     return  Product.objects.filter(pk=pk)



#function Based View
def product_detail_view(request,pk=None,*args,**kwargs):
    #instance = Product.objects.get(pk=pk,featured=True)  #id
    # instance = get_object_or_404(Product,pk=pk)

    # try:                                                       #here we creating exception
    #   instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")

    # print(instance)
    # qs = Product.objects.filter(id=pk)                           #these are the most effective way doing upper stuff
    #
    # #print(qs)
    # if qs.exists() and qs.count() ==1:    #len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")


    context = {
        'object' : instance
    }
    return render (request,"products/detail.html",context)
