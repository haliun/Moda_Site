"""moda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include,url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from moda import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required as auth
from moda.views import ClothesListView,ClothesDetialView,UserProfileDetailView,UserProfileEditView

admin.autodiscover()
import password_reset
urlpatterns = [

    url(r'^$', views.home,name='home'),
    url(r'^admin/',include(admin.site.urls)),

########Autincation#####################################################
    url(r'^ajax_login/',views.ajax_login,name="ajax_login"),
    url(r'^logout/',views.logout_user),
    url(r'^register/',views.register_user,name='register'),

#########Profile##################################################
    url(r'^users/(?P<slug>\w+)/$',UserProfileDetailView.as_view(),name="profile"),
    url(r'^edit_profile/$',auth(UserProfileEditView.as_view()),name="edit_profile"),
#############Password reset#################################################
    url(r'^user/password/reset/$', auth_views.password_reset, {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    url(r'^user/password/reset/done/$',auth_views.password_reset_done),
    url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', auth_views.password_reset_complete),

############Main menu: Goods ####################################################
    url(r'^goods/clothes/$',TemplateView.as_view(template_name="goods/clothes.html")),
    url(r'^goods/newarrivals/',TemplateView.as_view(template_name="goods/newarrivals.html")),
    url(r'^goods/accessories/',TemplateView.as_view(template_name="goods/accessories.html")),
    url(r'^goods/cosmetics/',TemplateView.as_view(template_name="goods/cosmetics.html")),
    url(r'^goods/sales/',TemplateView.as_view(template_name="goods/sales.html")),
    url(r'^goods/services/',TemplateView.as_view(template_name="goods/services.html")),
    url(r'^goods/shoes/',TemplateView.as_view(template_name="goods/shoes.html")),
    url(r'^news/',TemplateView.as_view(template_name="base site/news.html"),name='news'),

################Clothes#####################################################################
    url(r'^clothes/all/',ClothesListView.as_view(),name='all clothes'),
    url(r'^clothes_detial/(?P<pk>\d+)/$',ClothesDetialView.as_view(),name='clothes_detial'),

##########Footer menu##################################################################
    url(r'^aboutus/',TemplateView.as_view(template_name="base site/aboutus.html")),
    url(r'^terms/',TemplateView.as_view(template_name="base site/Terms.html")),
    url(r'^instructions/',TemplateView.as_view(template_name="base site/instructions.html")),
    url(r'^contact/',TemplateView.as_view(template_name="base site/contact.html")),
    url(r'^faq/',TemplateView.as_view(template_name="base site/Faq.html")),
    url(r'^sharewith/',TemplateView.as_view(template_name="base site/sharewith.html")),

############Main functions##################################################################
    url(r'^functions/events/',TemplateView.as_view(template_name="functions/events.html")),
    url(r'^functions/exchange/',TemplateView.as_view(template_name="functions/exchange.html")),
    url(r'^functions/forshops/',TemplateView.as_view(template_name="functions/forshops.html")),
    url(r'^functions/search/',TemplateView.as_view(template_name="functions/search.html")),
    url(r'^functions/present/',TemplateView.as_view(template_name="functions/present.html")),
    url(r'^uploadclothes/',views.upload_clothes ,name="uploadclothes"),
##################SEARCH###############################

   # url(r'^uploadcosmetic/','moda.views.upload_clothes',name='uploadclothes'),
    #url(r'^uploadshoes/','moda.views.upload_clothes',name='uploadclothes'),
   # url(r'^uploadaccessories/','moda.views.upload_clothes',name='uploadclothes'),
   # url(r'^functions/uploadclothes/$',ClothesUploadView.as_view(template_name="functions/uploadclothes.html")),
                         ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
             # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
