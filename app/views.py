from django.shortcuts import render,get_object_or_404,redirect
from .models import InteriorWork,GalleryImage,Contact,Blog,Featured_Blog,banner_Image,Services
from .forms import ContactForm





def Home(request):
    projects=InteriorWork.objects.order_by("-id")[:3]
    banner=banner_Image.objects.order_by("-id").first()
    return render(request,'index.html',{"banner":banner,"projects":projects})

def About(request):
    return render(request,'about.html')

def Service(request):
    Service=Services.objects.all()
    return render(request,'services.html',{"services":Service})

def blog(request):
    blog=Blog.objects.all()
    featured_blog=Featured_Blog.objects.order_by('-id').first()
    return render(request,'blog.html',{"blog":blog,"featured_blog":featured_blog})

def Projucts(request):
    projects=InteriorWork.objects.all()
    return render(request,'projucts.html',{"projects":projects})

def Projuct_details(request,id):
    projuct_details=get_object_or_404(InteriorWork,id=id)
    return render(request,'projuct-details.html',{'projuct':projuct_details})

def Ourshowroom(request):
    images=GalleryImage.objects.order_by("-id")[:6]
    return render(request,'ourshowroom.html',{"images":images})

from django.core.paginator import Paginator


def Gallery(request):
    images = GalleryImage.objects.order_by("-id")
    paginator = Paginator(images, 9) 
    
    page_number = request.GET.get("page") 
    page_obj = paginator.get_page(page_number)  
    
    return render(request, "gallery.html", {"page_obj": page_obj})


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