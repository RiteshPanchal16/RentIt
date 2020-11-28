from django.shortcuts import render ,HttpResponse
from myapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def home(request):
    return render(request,"index.html")

def Services(request):
    return render(request,"Services.html")

def properties(request):
    return render(request,"property.html")

def container(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        text_area=request.POST.get('text_area')
        image=request.POST.get('image')
        contact=Contact(name=name,email=email,phone=phone,text_area=text_area,image=image)
        contact.save()
        messages.success(request, 'your informtion has been submitted')

    return render(request,"container.html")
