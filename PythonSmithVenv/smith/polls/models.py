from django.db import models
from django. contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import reverse



 
class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
 
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
 
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class Users(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=20 )

class Post(models.Model):
    posted_by = models.CharField(max_length=30)
    post_content = models.CharField(max_length=20)
    publish_date = models.CharField(max_length=30)
    comments = models.CharField(max_length=20)

# class Post(models.Model):
#     commented_by = models.CharField(max_length=30)
#     commented_date= models.CharField(max_length=30)
#     Post = models.CharField(max_length=20)


 
class CustomUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True)
    USERNAME_FIELD = "username"
    objects = UserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True