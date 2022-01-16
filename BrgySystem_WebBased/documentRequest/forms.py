from django import forms
from accounts.models import User
from documentRequest.models  import docType,docRequest

class requestDocForm(forms.ModelForm):
    Document_Type =forms.ChoiceField(choices=docType.Document_Choices,label='Document Type')
    first_name = forms.CharField(required=True,label='First Name')
    last_name = forms.CharField(required=True,label='Last Name')
    middle_name = forms.CharField(required=False,label='Middle Name')
    age = forms.CharField(required=True)
    nationality = forms.CharField(required=True)
    purpose = forms.CharField(required=True)
    email = forms.EmailField()
    is_Pending = True
    class Meta:
        model=docRequest
        fields = ['Document_Type','first_name','last_name','middle_name','age','nationality',
                'purpose','Address','email','requested_by']
        widgets = {
            'requested_by': forms.TextInput(attrs={'class':'form','value':'','id':'elder','type':'hidden'}),
        }
