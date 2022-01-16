from django.shortcuts import render
from post.models import PostEvent

# Create your views here.
def staff_index(request):
    context = {}
    context["dataset"] = PostEvent.objects.all()
    return render(request,'Staff_index.html',context)

def staff_aboutus(request):
    return render(request,'staff_about.html')
