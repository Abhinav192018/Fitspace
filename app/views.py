from django.shortcuts import render,get_object_or_404,redirect
from .models import InteriorWork
# Create your views here.


def Home(request):
    return render(request,'index.html')

def About(request):
    return render(request,'about.html')

def Service(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def Projucts(request):
    projects=InteriorWork.objects.all()
    return render(request,'projucts.html',{"projects":projects})

def Projuct_details(request,id):
    projuct_details=get_object_or_404(InteriorWork,id=id)
    return render(request,'projuct-details.html',{'projuct':projuct_details})

def Ourshowroom(request):
    return render(request,'ourshowroom.html')

def Gallery(request):
    return render(request,"gallery.html")

def contact(request):
    return render(request,'contact.html')