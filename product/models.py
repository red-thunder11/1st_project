from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# # Create your models here.

class categories(models.Model):
    category_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100)
    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.category_name


class Products(models.Model):
    category = models.ForeignKey(categories,on_delete=models.PROTECT)
    author= models.ForeignKey(User,on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    price = models.IntegerField()
    specification = RichTextField()
    description = RichTextField()
    publish_date= models.DateTimeField(auto_now_add=True)
    upload_date= models.DateTimeField(auto_now=True)
    page_views= models.IntegerField(default=0)
    meta_title = models.CharField(max_length=100,null=True,blank=True)
    meta_description = models.CharField(max_length=100,null=True,blank=True)
    is_published= models.BooleanField(default=False)
    class Meta:
        verbose_name_plural="Products"


class company_details(models.Model):
    com_name = models.CharField(max_length=100)
    com_logo = models.ImageField(upload_to='photos/%Y/%m/%d')
    com_address = models.CharField(max_length=100)
    com_phone = models.IntegerField()
    com_email = models.EmailField(max_length=100)
    com_website = models.URLField(max_length=100)
    com_description = RichTextField()
    com_facebook = models.URLField(max_length=100)
    com_twitter = models.URLField(max_length=100)
    com_linked_in = models.URLField(max_length=100)
    com_instagram = models.URLField(max_length=100)
    com_youtube = models.URLField(max_length=100)
    def __str__(self):
        return self.com_name

    class Meta:
        verbose_name_plural="Companies"


class more_items(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100)
    class Meta:
        verbose_name_plural="Items"

    def __str__(self):
        return self.name


class banner(models.Model):
    name = RichTextField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d')

    class Meta:
        verbose_name_plural="Banners"


