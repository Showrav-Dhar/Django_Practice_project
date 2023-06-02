from django.urls import path
from products import views

#importing views from products folder

urlpatterns =[
    path('',views.index),
    path('new_fun',views.new_fun), 
    
]