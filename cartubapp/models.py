from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    catname = models.CharField(max_length=100,unique=True,primary_key=True)
    slug = models.SlugField(max_length=100,unique=True)
    img = models.ImageField(upload_to='photos')
    def __str__(self):
        return self.catname
    def get_url(self):
        return reverse('filter',args=[self.slug])
class products(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    img = models.ImageField(upload_to='albums')
    stock = models.IntegerField()
    available = models.BooleanField(default=False)
    categ = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name