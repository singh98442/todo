from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo_1.models import contact
from todo_1.models import blog
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def cont(request):
    if request.method=='POST':

        first_name1=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        city=request.POST['city']
        zip=request.POST['zip']

        

        ins=contact(first_name=first_name1,last_name=last_name,email=email,city=city,zip=zip)
        ins.save()

        messages.success(request,"successfully data stored")

    


    return render(request,'cont.html') 


def tasktable(request):
    tasked=contact.objects.all()
    context={'tasks':tasked}
    return render(request,'tasktable.html',context)

def blog1(request,slug):
    return HttpResponse(f"{slug}")  

def blogs(request):
    blo= blog.objects.all()
    context = {'blo':blo}
    return render(request,'blogs.html',context) 

def output(request):
    out1=blog.objects.filter()
    return render(request,'output.html')                