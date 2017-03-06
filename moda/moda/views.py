from django.shortcuts import render
import json
import csv
# Create your views here.
from django.utils.translation import ugettext
from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.conf import settings
from django.contrib import messages, auth
from django.template import RequestContext,loader
from datetime import datetime
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views.generic import UpdateView ,DetailView,ListView,FormView,DeleteView
from django.core.urlresolvers import reverse,reverse_lazy
from django.core.context_processors import csrf
from moda.models import Clothes,UserProfile
from moda.forms import Registrationform, UploadClothesForm, UserProfileForm
from django.contrib.auth.views import password_reset,password_reset_confirm
from django.http.response import HttpResponseForbidden,HttpResponseBadRequest,HttpResponseNotFound
from django.template import Context
from django.views.decorators.csrf import csrf_exempt
from django import shortcuts
from django.contrib.auth.decorators import login_required
import operator
from django.db.models import Q
def home(request):
    message = ugettext("Translated in the VIEWS and transmitted via context.")
    print ("Translated message=", message)
    context=RequestContext(request)
    context['message'] = message
    return render_to_response('base site/home.html',context)

######################AUTHINCATION USER#######################################
@csrf_exempt
def ajax_login(request):
    data = {}
    if request.method!="POST":
        return HttpResponseNotFound("<h1>Not Found</h1><p>The requested URL "+request.path)
    if 'username' not in request.POST or not request.POST['username']:
         data["result"] = "false"
         data["description"] = "Username is empty"
         return HttpResponse(json.dumps(data) )
    elif 'password'not in request.POST or not request.POST['username']:
         data["result"] = "false"
         data["description"] = "Password is empty"
         return HttpResponse(json.dumps(data) )
    try :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if not user is None:
             login(request, user)
             data["result"] = "true"
        else:
            data["result"] = "false"
            data["description"] = "user not found"
        print ( "data=" , data, json.dumps(data) )


    except  Exception as exp :
        print( str(exp) )
        data["result"] = "false"
        data["description"] = str( exp )
    return HttpResponse(json.dumps(data) )
def register_user(request):
    if request.method == 'POST':
        data = {}
        try :
            form=Registrationform(request.POST or None)
            if form.is_valid():
                u_name=form.cleaned_data.get('username')
                u_pass=form.cleaned_data.get('password2')
                form.save()
                user=authenticate(username=u_name, password=u_pass)
                user.backend="django.contrib.auth.backends.ModelBackend"
                login(request,user)
                data["result"] = "true"
            else:
                data["result"] = "false"
                data["description"] = "Something is wrong!!!"
            print ( "data=" , data, json.dumps(data) )
        except  Exception as exp :
            print( str(exp) )
            data["result"] = "false"
            data["description"] = str( exp )
        return HttpResponse(json.dumps(data))

def logout_user(request):
    data = {}
    logout(request)
    messages.info(request, "Successfully logged out.")
    data["result"] = "true"
    return HttpResponse(json.dumps(data) )
##############User profile###########################################
class UserProfileDetailView(DetailView):
    model=get_user_model()
    slug_field="username"
    template_name='registration/user_detail.html'

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user

class UserProfileEditView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name='registration/edit_profile.html'

    def get_object(self,queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]
    def get_success_url(self):
        return reverse("profile",kwargs={'slug':self.request.user})
###############PASSWORD RESET############################################3
def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='registration/password_reset_confirm.html',
        uidb64=uidb64, token=token,)
def reset(request):
    return password_reset(request, template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_done.html',
        subject_template_name='registration/reset_subject.txt')

##############Clothes functions##################################################################
def upload_clothes(request):
    data = {}
    clothes_name=request.GET['clothes_name']
    clothes_size=request.GET['clothes_size']
    clothes_type=request.GET['clothes_type']
    clothes_gender=request.GET['clothes_gender']
    clothes_brand=request.GET['clothes_brand']
    clothes_material=request.GET['clothes_material']
    clothes_season=request.GET['clothes_season']
    clothes_price=request.GET['clothes_price']
    clothes_situation=request.GET['clothes_situation']
    clothes_description=request.GET['clothes_description']
    clothes_color=request.GET['clothes_color']
    clothes_image=request.GET['clothes_image']
    owner_telephone=request.GET['owner_telephone']
    clothes_delivery=request.GET['clothes_delivery']
    want_sell='want_sell' in request.GET
    want_swap='want_swap' in request.GET
    clothes=Clothes(
        clothes_name=clothes_name,
        clothes_brand=clothes_brand,
        clothes_color=clothes_color,
        clothes_description=clothes_description,
        clothes_gender=clothes_gender,
        clothes_image=clothes_image,
        clothes_material=clothes_material,
        clothes_price=clothes_price,
        clothes_season=clothes_season,
        clothes_size=clothes_size,
        clothes_situation=clothes_situation,
        clothes_type=clothes_type,
        owner=request.user,
        clothes_dateupload=datetime.now(),
        want_sell=want_sell,
        want_swap=want_swap,
        owner_telephone=owner_telephone,
        clothes_delivery=clothes_delivery,
        )
    clothes.save()
    return HttpResponse(json.dumps(data))

class ClothesListView(ListView):
    model=Clothes
    queryset = Clothes.objects.order_by('-clothes_dateupload')
    context_object_name = "clothes"
    template_name = "goods/clothes_list.html"
    paginate_by = 10
class ClothesDetialView(DetailView):
    model=Clothes
    template_name = "goods/clothes_detial.html"


## class SearchQuerySet(models.query.QuerySet):
#      def __init__(self, model=None, fields=None):
#          super(SearchQuerySet, self).__init__(model)
#          self._search_fields = fields
#
#      def search(self, query):
#          meta = self.model._meta
#
#          # Get the table name and column names from the model
#          # in `table_name`.`column_name` style
#          columns = [meta.get_field(name,
#                                              many_to_many=False).column
#              for name in self._search_fields]
#          full_names = ["%s.%s" %
#                         (backend.quote_name(meta.db_table),
#                          backend.quote_name(column))
#                          for column in columns]
#
#          # Create the MATCH...AGAINST expressions
#          fulltext_columns = ", ".join(full_names)
#          match_expr = ("MATCH(%s) AGAINST (%%s)" %
#                                 fulltext_columns)
#
#          # Add the extra SELECT and WHERE options
#          return self.extra(select={'relevance': match_expr},
#                                  where=[match_expr],
#                                  params=[query, query])
#
#
# class SearchManager(models.Manager):
#      def __init__(self, fields):
#          super(SearchManager, self).__init__()
#          self._search_fields = fields
#
#      def get_query_set(self):
#          return SearchQuerySet(self.model, self._search_fields)
#
#      def search(self, query):
#          return self.get_query_set().search(query)