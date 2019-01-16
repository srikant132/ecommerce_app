""" python manage.py shell """
>>> from tags.models import Tag
>>> Tag.objects.all()
<QuerySet [<Tag: Tube-Light>, <Tag: TubeLight>, <Tag: white>, <Tag: yellow>, <Tag: red>]>
>>> Tag.objects.last()
<Tag: red>
>>> red = Tag.objects.last()
>>> red.title
'red'

red.slug
'ded'

red.active
True

red.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x7f2313747a20>
red.products.all()
<ProductQuerySet [<Product: Hat>]>
red.products.all().first()
<Product: Hat>


from products.models import Product
qs = Product.objects.all()
qs
<ProductQuerySet [<Product: Hat>, <Product: Shoes>, <Product: bedsheet>, <Product: Tube-Light>, <Product: Lorem Ipsum>, <Product: hat>
]>

 tshirt = qs.first()
 tshirt
<Product: Hat>
 tshirt.title
'Hat'
