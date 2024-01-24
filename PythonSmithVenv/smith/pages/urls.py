from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name= "Home"),
    path('policy',views.policy, name= "Policy"),
    path('terms',views.terms, name = "Terms"),
    path('shop',views.shop, name = "Shop"),
    path('cart',views.cart, name = "Cart"),
    path('profile',views.profile, name = "Profile")
    ]