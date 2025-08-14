from django.shortcuts import render,get_object_or_404,redirect
from .models import InteriorWork,GalleryImage,Contact
from .forms import ContactForm





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
    images=GalleryImage.objects.order_by("-id")[:6]
    return render(request,'ourshowroom.html',{"images":images})

def Gallery(request):
    images=GalleryImage.objects.order_by("-id")
    return render(request,"gallery.html",{"images":images})


from django.contrib import messages
def contact(request):
    if request.method == 'POST':
        Contact.objects.create(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        messages.success(request, "Your message was sent successfully")
        return redirect('contact')
    return render(request, 'contact.html')