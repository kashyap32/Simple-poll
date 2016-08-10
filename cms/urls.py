from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from . import views

urlpatterns = [
    url(r'^$', LogIn, name = 'login'),
    url(r'^signup/', SignUp, name = 'signup'),
    url(r'^home/', Home, name = 'home'),
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name="detail"),

    url(r'^(?P<question_id>[0-9]+)/results$',views.results,name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote$',views.vote,name="vote"),
]
