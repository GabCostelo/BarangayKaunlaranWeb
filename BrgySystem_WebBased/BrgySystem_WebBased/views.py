from django.shortcuts import render
from post.models import PostEvent

def index(request):
    context = {}
    context["dataset"] = PostEvent.objects.all()
    return render(request,'index.html',context)

def aboutus(request):
    return render(request,'aboutus.html')
