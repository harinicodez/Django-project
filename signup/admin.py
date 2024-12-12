from django.contrib import admin

# Register your models here.
from .models import Blog, Bloguser
admin.site.register(Blog)
admin.site.register(Bloguser)
