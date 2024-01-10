from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=20 )

# class Post(models.Model):
#     posted_by = models.CharField(max_length=30)
#     post_content = models.CharField(max_length=20, required=True)
#     publish_date = models.CharField(max_length=30)
#     comments = models.CharField(max_length=20)

# class Post(models.Model):
#     commented_by = models.CharField(max_length=30)
#     commented_date= models.CharField(max_length=30)
#     Post = models.CharField(max_length=20)

