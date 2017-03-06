__author__ = 'haliun'
from django import forms
from moda.models import Clothes,Shoes,Accessories,Makeup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.contenttypes.models import ContentType

class Registrationform(UserCreationForm):
    email=forms.EmailField(required=True)
   # telephone=forms.CharField(required=True)
    class Meta:
        model=User
        fields=('username','first_name','last_name','password1','password2')
    def save(self,commit=True):
            user=super(Registrationform,self).save(commit=False)
            user.email=self.cleaned_data['email']
           # user.telephone=self.cleaned_data['telephone']

            if commit:
                user.save()
            return user
class UploadClothesForm(forms.ModelForm):
     class Meta:
        model=Clothes
        fields=('clothes_name','clothes_size','clothes_material','clothes_type','clothes_color','clothes_gender','clothes_brand','clothes_image','clothes_price','clothes_situation','clothes_season','clothes_description')

class UploadShoesForm(forms.ModelForm):
     class Meta:
        model=Shoes
        fields='__all__'
class UploadAccForm(forms.ModelForm):
    class Meta:
        model=Accessories
        fields='__all__'
class UploadMakeup(forms.ModelForm):
    class Meta:
        model=Makeup
        fields='__all__'


