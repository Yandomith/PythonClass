from django.urls import path

from . import views

urlpatterns = [
    path("home", views.index, name="index"),
    path("contact", views.read_data, name="contact"),
    path("pagal", views.new_data, name="services"),
    path("form",views.form,name="form" ),
    path("profile",views.profile, name= "profile"),
    path("createprofile",views.post_form, name= "createPost")
]