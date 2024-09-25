
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name= 'index'),
    path('prod_list', views.prod_list, name = 'prod-list'),
    path('prod_detail/<slug>/', views.prod_detail, name = 'prod-detail'),
    path('prod_category/<slug>/', views.prod_category, name = 'prod-category'),
    path("search", views.search,name = "search"),
    path("privacy_policy", views.privacy_policy, name="privacy-policy"),
    path("terms_conditions", views.terms_conditions, name="terms-conditions"),
    path("about_us", views.about_us, name="about-us")
]

