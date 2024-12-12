from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=350)
    description = models.CharField(max_length=500)
    image_url = models.URLField(max_length=250)
    data = models.TextField(max_length=3000, default='') 
    created_at = models.DateTimeField(auto_now_add=True)


class Bloguser(models.Model):
    name = models.CharField(max_length=250)
    email_address = models.EmailField(max_length=250)  
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)