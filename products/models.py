import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils  import  unique_slug_generator
from django.urls import reverse


#here it create the new filename extension
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext

# Create your models here.

#here it create new file name with using some random integer betn the value

def upload_image_path(instace,filename):
    # print(instance)
    # print(filename)
    new_filename = random.randint(1,4655624541)
    name,ext = get_filename_ext(filename)
    final_filename = f'{ new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,                        #it gives us more robust way of the  file name
            final_filename=final_filename
        )

#here  w creatin a function for ProductManager

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):          #Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self,id):
        qs = self.get_queryset().filter(id=id)                                #this portion takes Product.objects ==  self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None



class Product(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True,unique=True)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image       = models.ImageField(upload_to='upload_image_path',null=True, blank=True)
    featured    = models.BooleanField(default=False)
    active      = models.BooleanField(default=True)



    objects = ProductManager()

    #it create the obsolute url to get product                                                          #it's a function that rep of model it's instance field
    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("detail",kwargs={"slug":self.slug })               #here we are using  reverse urlutility funcyons


    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
#here we are generating slug
def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug =unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=Product)
