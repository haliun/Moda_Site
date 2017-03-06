# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessories',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('acc_name', models.CharField(max_length=30)),
                ('acc_gender', models.CharField(max_length=10)),
                ('acc_type', models.CharField(max_length=15)),
                ('acc_brand', models.CharField(max_length=20)),
                ('acc_material', models.CharField(max_length=30)),
                ('acc_image', models.FileField(upload_to='.')),
                ('acc_color', models.CharField(max_length=15)),
                ('acc_situation', models.CharField(max_length=10)),
                ('acc_price', models.CharField(max_length=20)),
                ('acc_description', models.CharField(max_length=200)),
                ('acc_data_upload', models.DateTimeField(auto_now_add=True)),
                ('acc_delivery', models.CharField(max_length=20)),
                ('want_sell', models.BooleanField(default=False)),
                ('want_swap', models.BooleanField(default=False)),
                ('owner_telephone', models.CharField(max_length=20)),
                ('owner', models.ForeignKey(db_column='owner_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'accessories',
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('clothes_name', models.CharField(max_length=30)),
                ('clothes_size', models.CharField(max_length=3)),
                ('clothes_dateupload', models.DateTimeField(auto_now_add=True)),
                ('clothes_gender', models.CharField(max_length=10)),
                ('clothes_type', models.CharField(max_length=25)),
                ('clothes_brand', models.CharField(max_length=20)),
                ('clothes_material', models.CharField(max_length=20)),
                ('clothes_image', models.ImageField(upload_to='/uploaded_clothes')),
                ('clothes_color', models.CharField(max_length=15)),
                ('clothes_situation', models.CharField(max_length=15)),
                ('clothes_price', models.CharField(max_length=20)),
                ('clothes_season', models.CharField(max_length=15)),
                ('clothes_description', models.CharField(max_length=200)),
                ('clothes_delivery', models.CharField(max_length=20)),
                ('want_sell', models.BooleanField(default=False)),
                ('want_swap', models.BooleanField(default=False)),
                ('owner_telephone', models.CharField(default=0, max_length=20)),
                ('owner', models.ForeignKey(db_column='owner_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='Makeup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('makeup_name', models.CharField(max_length=30)),
                ('makeup_type', models.CharField(max_length=25)),
                ('makeup_brand', models.CharField(max_length=20)),
                ('makeup_image', models.FileField(upload_to='.')),
                ('makeup_situation', models.CharField(max_length=10)),
                ('makeup_price', models.CharField(max_length=20)),
                ('makeup_data_upload', models.DateTimeField(auto_now_add=True)),
                ('makeup_description', models.CharField(max_length=200)),
                ('makeup_delivery', models.CharField(max_length=20)),
                ('want_sell', models.BooleanField(default=False)),
                ('want_swap', models.BooleanField(default=False)),
                ('owner_telephone', models.CharField(default=0, max_length=20)),
                ('owner', models.ForeignKey(db_column='owner_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'makeup',
            },
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('shoes_name', models.CharField(max_length=30)),
                ('shoes_dataupload', models.DateTimeField(auto_now_add=True)),
                ('shoes_size', models.CharField(max_length=3)),
                ('shoes_gender', models.CharField(max_length=10)),
                ('shoes_type', models.CharField(max_length=25)),
                ('shoes_brand', models.CharField(max_length=20)),
                ('shoes_material', models.CharField(max_length=20)),
                ('shoes_image', models.FileField(upload_to='.')),
                ('shoes_color', models.CharField(max_length=15)),
                ('shoes_situation', models.CharField(max_length=10)),
                ('shoes_price', models.CharField(max_length=20)),
                ('shoes_season', models.CharField(max_length=10)),
                ('shoes_description', models.CharField(max_length=200)),
                ('shoes_delivery', models.CharField(max_length=20)),
                ('want_sell', models.BooleanField(default=False)),
                ('want_swap', models.BooleanField(default=False)),
                ('owner_telephone', models.CharField(default=0, max_length=20)),
                ('owner', models.ForeignKey(db_column='owner_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shoes',
            },
        ),
    ]
