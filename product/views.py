from django.shortcuts import render
from . import models
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):
    data = {
        'banner_info' : models.banner.objects.all(),
        'featured' : models.Products.objects.filter(is_published = True).order_by('?'),
    }
    return render(request,"pages/index.html", data)

def prod_list(request):
    # pagination start
    product = models.Products.objects.filter(is_published = True).all()
    pagination = Paginator(product,6)
    page = request.GET.get('page')
    productFinal = pagination.get_page(page)
    # pagination end

    data = {
        "product" : productFinal,
        'featured' : models.Products.objects.filter(is_published = True).order_by("?"),
    }
    return render(request, "pages/prod_list.html", data)


def prod_detail(request,slug):
    pobj = models.Products.objects.get(slug=slug)
    category = pobj.category
    data = {
        "product" : models.Products.objects.get( slug = slug),
        'related' : models.Products.objects.filter(category=category).exclude(slug=slug).order_by("?")[:5],
    }
    return render(request, 'pages/prod_detail.html', data)


def search(request):
    query = request.GET.get("search")
    data = {
        'prod_search' : models.Products.objects.filter(Q(slug__icontains = query) | Q(name__icontains = query) | Q(description__icontains = query) | Q(category__category_name__icontains = query))
    }
    return render(request, "pages/search.html", data)

def prod_category(request, slug):
    category = models.categories.objects.get(slug=slug)

    data = {
        'prod_category' : models.Products.objects.filter(category=category)
    }

    return render(request, 'pages/category.html', data)


def privacy_policy(request):
    return render(request,"pages/privacy_policy.html")


def terms_conditions(request):
    return render(request,"pages/terms_conditions.html")


def about_us(request):
    return render(request,"pages/about_us.html")