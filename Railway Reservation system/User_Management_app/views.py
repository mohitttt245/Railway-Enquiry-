from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        Pass1=request.POST.get('Password1')
        pass2=request.POST.get('Password2')

        if Pass1!=pass2:
            return HttpResponse("Your password and confirmation password are not same!")
        else:
            my_user=User.objects.create_user(uname,Pass1)
            my_user.save()
            return redirect('login')
    return render (request,'register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('Password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('user')
        else:
            return HttpResponse("Username or password is incorrect")
    return render (request,'login page.html')
