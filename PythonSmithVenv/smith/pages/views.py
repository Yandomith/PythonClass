from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"index.html")

def policy (request):
    return render (request, "policy.html")

def terms (request):
    return render (request, "terms.html")

def shop (request):
    return render (request, "shop.html")


def cart (request):
    return render (request, "cart.html")

def profile (request):
    return render (request, "profile.html")

# PythonSmithVenv/smith/pages/templates/index.html