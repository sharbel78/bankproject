from  . import  views
from django.urls import path
app_name="bankapp"
urlpatterns = [

    path('',views.demo,name='demo'),
    path('login', views.login, name='login'),
    path('register',views.register,name='register'),

    path('button', views.single, name='single'),
    path('form', views.form, name='form'),





]