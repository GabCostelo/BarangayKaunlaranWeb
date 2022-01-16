from django.urls import path

from . import views

app_name = 'Records'

urlpatterns = [
    path('records/',views.recordIndex,name='recordIndex'),
    path('recordUser/',views.recordUser,name='userRecord'),
    path('recordDoc/',views.recordDoc,name='docRecord'),
    path('recordUserList/',views.Userlist,name='userList'),
    path('recordStaffList/',views.StaffList,name='staffList'),
    path('recordConsList/',views.ConsList,name='consList'),
    path('recordsIndigency',views.IndigencyList,name='listIndigency'),
    path('recordsClearance',views.ClearanceList,name='listClearance'),
    path('recordsResidency',views.ResidencyList,name='listResidency'),
]
