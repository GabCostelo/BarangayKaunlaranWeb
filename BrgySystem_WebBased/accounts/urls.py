from django.urls import path
from django.contrib.auth import views

from . import views

app_name = 'Accounts'
urlpatterns = [
    path('login/',views.user_login,name='login'),
    path('register/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('staffLogin/',views.staff_login,name='Stafflogin'),
    path('staffLogout/',views.staff_logout,name='Stafflogout'),
    path('staffRegister/',views.staff_signup,name='StaffRegister')
]
