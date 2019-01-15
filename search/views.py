from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
# Create your views here.

class SearchProductView(ListView):
    template_name = "search/view.html"

    def get_context_data(self,*args,**kwargs):
       context = super(SearchProductView,self).get_context_data(*args,**kwargs)
       query = self.request.GET.get('q')
       context['query'] = query
       # SearchQuery.objects.create(query=query)
       return context


    def get_queryset(self,*args,**kwargs):
        request = self.request
        method_dict = request.GET     # it something like python dict
        query = method_dict.get('q', None)
        if query is not None:
            return  Product.objects.search(query)   #it differantiat with both if both have same
        return Product.objects.featured()


'''
__icontains = field contains this
__iexact = field is exactly this

'''
