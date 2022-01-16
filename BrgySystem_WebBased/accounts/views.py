from django.shortcuts import render
from accounts.forms import ConstituentCreateForm,StaffCreateForm

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                if user.is_Constituent:
                    login(request,user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    return HttpResponse('Not Constituent Account!')
            else:
                return HttpResponse('Account Not Active!')
        else:
            print('Login Failed!')
            print("Username:{} and password: {}.".format(username,password))
            return HttpResponse("Invalid Login Details")
    else:
        return render(request,'login.html',{})

def user_signup(request):
    if request.method == 'POST':
        user_form = ConstituentCreateForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()
            return render(request,'login.html')
        else:
            print(user_form.errors)
    else:
        user_form = ConstituentCreateForm

    return render(request,'register.html',{'user_form':user_form})

@login_required
def staff_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Staff:staff_home'))

def staff_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                if user.is_BrgyStaff:
                    login(request,user)
                    return HttpResponseRedirect(reverse('Staff:staff_home'))
                else:
                    return HttpResponse('Not Barangay Staff Account!')
            else:
                return HttpResponse('Account Not Active!')
        else:
            print('Login Failed!')
            print("Username:{} and password: {}.".format(username,password))
            return HttpResponse("Invalid Login Details")
    else:
        return render(request,'staff_login.html',{})

def staff_signup(request):
    if request.method == 'POST':
        staff_form = StaffCreateForm(data=request.POST)

        if staff_form.is_valid():
            user = staff_form.save()
            user.save()
            return render(request,'staff_login.html')
        else:
            print(staff_form.errors)
    else:
        staff_form = StaffCreateForm

    return render(request,'staff_register.html',{'staff_form':staff_form})
