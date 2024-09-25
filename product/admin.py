from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(categories)
class categoriesAdmin(admin.ModelAdmin):
    list_display = ["category_name" , "slug"]
    prepopulated_fields = {'slug' : ("category_name",)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['category', "author", "name" , "slug","publish_date" , 'page_views']
    prepopulated_fields = {'slug' : ("name",)}
    list_filter = ['category', "author", "publish_date" ]
    search_field = ['category', "description" ]


@admin.register(company_details)
class company_detailsAdmin(admin.ModelAdmin):
    list_display = ['com_name', "com_address", "com_email" ]
    list_filter = ['com_name', "com_address", "com_email" ]
    search_field = ['com_name', "description" ]


@admin.register(more_items)
class more_itemsAdmin(admin.ModelAdmin):
    list_display = ["name" , "slug"]
    prepopulated_fields = {'slug' : ("name",)}

@admin.register(banner)
class more_itemsAdmin(admin.ModelAdmin):
    list_display = ["name"]


