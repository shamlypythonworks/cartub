from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# import tkinter.messagebox
# Create your views here.
def register(request):

    if request.method == "POST" and 'reg' in request.POST:
                first_name = request.POST.get('name')
                username = request.POST.get('username')
                email = request.POST.get('email')
                password = request.POST.get('psw')
                repassword = request.POST.get('psw_repeat')
                if password == repassword:
                    if User.objects.filter(username=username).exists():
                        messages.info(request,'username already exists')
                        return redirect('register')
                    elif User.objects.filter(email=email).exists():
                        messages.info(request,"email already exists")
                        return redirect('register')
                    else:
                        user = User.objects.create_user(first_name=first_name,username=username,email=email,password=password)
                        user.save()
                        messages.info(request,"account created")
                        return redirect('register')
                else:
                    messages.info(request, "password mismatch")
                    return redirect('register')
    else:
        return render(request,'registeration.html')
def login(request):
    if request.method == "POST" and 'lgin' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "username or password incorrect")
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')



