from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from accounts.models import User,BrgyStaff,Constituent

class StaffCreateForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_staff = True
        user.is_BrgyStaff = True
        user.save()
        staff = BrgyStaff.objects.create(user=user)
        staff.email = self.cleaned_data.get('email')
        staff.save()
        return user


class ConstituentCreateForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True,label='First Name')
    last_name = forms.CharField(required=True,label='Last Name')


    class Meta(UserCreationForm.Meta):
        model = User
        fields =['email','first_name','last_name','username']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.is_Constituent = True
        user.save()
        constituent = Constituent.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        constituent.save()
        return user
