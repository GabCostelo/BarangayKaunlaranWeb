from django.urls import path,include
from django.contrib.auth import views

from . import views


app_name = 'Staff'
urlpatterns = [
    path('',views.staff_index,name='staff_home'),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('events/',include('post.urls',namespace='post')),
    path('events/',include('django.contrib.auth.urls')),
    path('docu_Request/',include('documentRequest.urls',namespace='docuRequest')),
    path('docu_Request/',include('django.contrib.auth.urls')),
    path('records/',include('records.urls',namespace='records')),
    path('records/',include('django.contrib.auth.urls')),
    path('staffabout/',views.staff_aboutus,name='staffabout'),
]
