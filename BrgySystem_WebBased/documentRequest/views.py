from django.shortcuts import render,get_object_or_404
from documentRequest.forms import requestDocForm
from documentRequest.models import docRequest
from django.views.generic import DetailView
from accounts.models import Constituent

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def docRequestView(request):

    if request.method == 'POST':
        docReq_form = requestDocForm(data=request.POST)
        if docReq_form.is_valid():
            docReq_form.save(commit=False)
            docRequest.is_Pending=True
            docReq_form.save()
            return render(request,'index.html')
        else:
            print(docReq_form.errors)
    else:
        docReq_form = requestDocForm

    return render(request,'docReq.html',{'docReq_form':docReq_form})

def updateReq(request,pk):
    context = {}
    obj = get_object_or_404(docRequest, pk=pk)
    doneform = requestDocForm(data=request.POST or None,instance=obj)
    if doneform.is_valid():
        doneform.save(commit=False)
        obj.is_Pending = False
        obj.is_Done = True
        doneform.save()
        context["dataset"]=docRequest.objects.all
        return render(request,'staff_view.html',context)
    else:
        print(doneform.errors)
    return render(request,'update_view.html',{'doneform':doneform})

def docRequestList(request):
    context = {}
    context["dataset"] = docRequest.objects.filter(is_Pending=True)
    return render(request,'Staff_view.html',context)

class generatePdf(DetailView):
    model = docRequest
    template_name = 'certificate.html'

class generatePdfClearance(DetailView):
    model = docRequest
    template_name = 'clearance.html'

class generatePdfResidency(DetailView):
    model = docRequest
    template_name = 'residency.html'

def sendUpdate(request,pk):
    context={}
    context["data"] = docRequest.objects.get(pk=pk)
    if request.method == 'POST':
        bodySubject = request.POST.get('StatusBody')
        em = request.POST.get('emailParam')
        subject = 'Document Request Update'
        message = bodySubject
        email_from = settings.EMAIL_HOST_USER
        recipient_list =[em,]
        send_mail( subject, message, email_from, recipient_list , fail_silently = False)
        return render(request,'Staff_view.html',context)

    return render(request,'sendStatus.html',context)
