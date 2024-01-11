from django.contrib import admin
from .models import Post
from .models import Users

# # Register your models here.
# class MemberUsers(admin.ModelAdmin):
#   list_display = ("firstname", "lastname" )

admin.site.register(Post)
admin.site.register(Users, )