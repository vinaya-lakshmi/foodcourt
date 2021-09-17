from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class categs(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class products1(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    img=models.ImageField(upload_to='products')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categs,on_delete=models.CASCADE)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('details', args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name)



