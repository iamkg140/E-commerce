from django.urls import path, include
from django.conf.urls import url
from . import views

#Django admin header customiztaion

urlpatterns = [
    path('',views.home, name="home"),

    path('contact',views.contact, name="contact"),
    path('products',views.products, name="products"),
    path('single/<int:pk>/',views.single, name="single"),
    path('brochure',views.brochure, name="brochure"),
    path('searchbar',views.searchbar, name="searchbar"),
    path('checkout/<int:pk>/',views.checkout, name="checkout"), #paila single bata form submit garda checkout ma janxa
    path('complete-checkout',views.completeCheckout, name="complete-checkout"), #chcekout ko form submit huda completema janxa
]
