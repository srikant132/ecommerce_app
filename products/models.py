import random
import os
from django.db import models

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
            new_filename=new_filename,
            final_filename=final_filename               #it gives us more robust way of the  file name
        )


class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image       = models.ImageField(upload_to='upload_image_path',null=True, blank=True)
 #it's a function that rep of model it's instance field
 #it create the product instace different name with their title
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
