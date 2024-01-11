from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Users, Post
from .form import PostCreateForm 


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    context= {"first_name": "smith" ,"last_name":"haha"}
    return render(request,'index.html',context)

def read_data(request):
    user= Users.objects.get(username= "mithyando")
    context= {"first_name":user.first_name ,"last_name":user.last_name, "username":user.username}
    return render (request, "main.html",context)

def new_data(request):
    user= Users.objects.get(username= "pagal")
    context= {"first_name":user.first_name ,"last_name":user.last_name, "username":user.username}
    return render (request, "main.html",context)


def form(request):
    return render(request , "form.html")


def  profile(request):
    print("****************")
    # print(request.POST)
    
    firstName= request.POST["first_name"]
    middleName= request.POST["middle_name"]
    lastName= request.POST["last_name"]
    userName= request.POST["username"]
    email= request.POST["email"]
    password= request.POST["password"]
    
    print("Processing Form.............")
    context= {"first name":firstName,"middle name ": middleName, "lastname ":lastName,"username": userName, "email":email, "password":password}
    new_user= Users(first_name=firstName,middle_name= middleName,  last_name= lastName,username= userName, email=email, password=password)
    new_user.save()
    return render(request,"profile.html",context)
    
def post_form(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("createprofile")
    else:
        form = PostCreateForm()
    return render (request, "createPost.html", context={"form":form})


class PostListView(generic.ListView):
    model= Post
    context_object_name="post_list"
    template_name = "post_list.html"

