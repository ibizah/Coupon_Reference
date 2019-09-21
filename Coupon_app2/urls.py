from django.urls import path
from . import views
app_name= 'Coupon_app2'
urlpatterns =[

path('', views.form, name='form'),
path('details/', views.details, name='details'),


 ]
