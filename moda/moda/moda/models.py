#-*- codinf: UTF-8 -*-
__author__ = 'haliun'
from django.db import models
# Create your models here.
from datetime import  datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Clothes(models.Model):

    clothes_name=models.CharField(max_length=30)
    clothes_size=models.CharField(max_length=3)
    clothes_dateupload=models.DateTimeField(auto_now_add=True)
    clothes_gender=models.CharField(max_length=10)
    clothes_type=models.CharField(max_length=25)
    clothes_brand=models.CharField(max_length=20)
    clothes_material=models.CharField(max_length=20)
    clothes_image=models.ImageField(upload_to='/uploaded_clothes')
    clothes_color=models.CharField(max_length=15)
    clothes_situation=models.CharField(max_length=15)
    clothes_price=models.CharField(max_length=20)
    clothes_season=models.CharField(max_length=15)
    clothes_description=models.CharField(max_length=200)
    clothes_delivery=models.CharField(max_length=20)
    want_sell=models.BooleanField(default=False)
    want_swap=models.BooleanField(default=False)
    owner=models.ForeignKey(User, to_field="id", db_column="owner_id", null=False)
    owner_telephone=models.CharField(max_length=20,default=0)
    def __unicode__(self):
        return self.clothes_name
    class Meta():
        db_table="clothes"
        app_label = "moda"


class Shoes(models.Model):
    shoes_name=models.CharField(max_length=30)
    shoes_dataupload=models.DateTimeField(auto_now_add=True)
    shoes_size=models.CharField(max_length=3)
    shoes_gender=models.CharField(max_length=10)
    shoes_type=models.CharField(max_length=25)
    shoes_brand=models.CharField(max_length=20)
    shoes_material=models.CharField(max_length=20)
    shoes_image=models.FileField(upload_to='.')
    shoes_color=models.CharField(max_length=15)
    shoes_situation=models.CharField(max_length=10)
    shoes_price=models.CharField(max_length=20)
    shoes_season=models.CharField(max_length=10)
    shoes_description=models.CharField(max_length=200)
    shoes_delivery=models.CharField(max_length=20)
    want_sell=models.BooleanField(default=False)
    want_swap=models.BooleanField(default=False)
    owner=models.ForeignKey(User, to_field="id", db_column="owner_id", null=False)
    owner_telephone=models.CharField(max_length=20,default=0)
    class Meta():
        db_table="shoes"
        app_label = "moda"

    def __unicode__(self):
        return '%s' % self.shoes_name
class Accessories(models.Model):
    acc_name=models.CharField(max_length=30)
    acc_gender=models.CharField(max_length=10)
    acc_type=models.CharField(max_length=15)
    acc_brand=models.CharField(max_length=20)
    acc_material=models.CharField(max_length=30)
    acc_image=models.FileField(upload_to='.')
    acc_color=models.CharField(max_length=15)
    acc_situation=models.CharField(max_length=10)#new, old, how old
    acc_price=models.CharField(max_length=20)
    acc_description=models.CharField(max_length=200)
    acc_data_upload=models.DateTimeField(auto_now_add=True)
    acc_delivery=models.CharField(max_length=20)
    want_sell=models.BooleanField(default=False)
    want_swap=models.BooleanField(default=False)
    owner=models.ForeignKey(User, to_field="id", db_column="owner_id", null=False)
    owner_telephone=models.CharField(max_length=20)
    class Meta():
        db_table="accessories"
        app_label = "moda"

    def __unicode__(self):
        return '%s' % self.acc_name
class Makeup(models.Model):
    makeup_name=models.CharField(max_length=30)
    makeup_type=models.CharField(max_length=25)

    makeup_brand=models.CharField(max_length=20)
    makeup_image=models.FileField(upload_to='.')
    makeup_situation=models.CharField(max_length=10)#new, old, how old
    makeup_price=models.CharField(max_length=20)
    makeup_data_upload=models.DateTimeField(auto_now_add=True)
    makeup_description=models.CharField(max_length=200)
    makeup_delivery=models.CharField(max_length=20)
    want_sell=models.BooleanField(default=False)
    want_swap=models.BooleanField(default=False)
    owner=models.ForeignKey(User, to_field="id", db_column="owner_id", null=False)
    owner_telephone=models.CharField(max_length=20,default=0)
    class Meta():
        db_table="makeup"
        app_label = "moda"

    def __unicode__(self):
        return '%s' % self.makeup_name


#class ClothesGroup(models.Model):
 #   name = models.CharField()
  #  ...