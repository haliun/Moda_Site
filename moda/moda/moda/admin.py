__author__ = 'haliun'
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from moda.models import Clothes,Shoes,Accessories,Makeup,UserProfile


admin.site.register(Clothes)
admin.site.register(Shoes)
admin.site.register(Accessories)
admin.site.register(Makeup)
admin.site.register(UserProfile)
