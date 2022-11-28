from pydoc import describe
from django.shortcuts import render,redirect
import random
from hospital.models import Hospital,Docter
from myapp.models import User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def hospitalindex(request):
    return render(request,'hospitalindex.html')


def hospitallogin(request):
    if request.method=='POST':
        try:
            Hospital.objects.get(email=request.POST['email'] , password=request.POST['password'])

            return redirect('hospitalindex') 
        except:
            return render(request,'hospitallogin.html',{'msg':'User not found'})

    return render(request,'hospitallogin.html')

def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'login.html')
    return render(request,'login.html')

def docter(request):
    data=Docter.objects.all()
    serdata={
        'data': data
    }
    return render(request,'docter.html',serdata)


def register(request):
    if request.method=='POST':
        Docter.objects.create(
        f_name=request.POST['f_name'],
        l_name=request.POST['l_name'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        password=request.POST['password'],
        specilist=request.POST['specilist'],
        pic=request.FILES['pic']
        )
        return redirect('docter')
    return render(request,'register.html')    


def delete(request,pid):
    dele=Docter.objects.get(id=pid)
    dele.delete()
    return redirect('docter')

def edit(request,id):
    obj=Docter.objects.get(id=id)
    if request.method=='POST':
        if 'pic' in request.FILES:
            obj.f_name=request.POST['f_name']
            obj.l_name=request.POST['l_name']
            obj.email=request.POST['email']
            obj.mobile=request.POST['mobile']
            obj.password=request.POST['password']
            obj.specilist=request.POST['specilist']
            obj.pic=request.FILES['pic']
            obj.save()
            return redirect('docter')
        else:
            obj.f_name=request.POST['f_name']
            obj.l_name=request.POST['l_name']
            obj.email=request.POST['email']
            obj.mobile=request.POST['mobile']
            obj.password=request.POST['password']
            obj.specilist=request.POST['specilist']
            obj.save()
            return redirect('docter')
    return render(request,'edit.html',{'pobj':obj})


def patient(request):
    ddd=User.objects.all()
    ff={
        'ddd':ddd
    }
    return render(request,'patient.html',ff)

def delet(request,id):
    dele=User.objects.get(id=id)
    dele.delete()
    return redirect('patient')
