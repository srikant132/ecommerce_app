from django.conf.urls import url


from carts.views import ( cart_home,
                             cart_update,

                         )

urlpatterns = [
    url(r'^$', cart_home, name='cart_home'),
    url(r'^update/$', cart_update ,name='update'),

]
