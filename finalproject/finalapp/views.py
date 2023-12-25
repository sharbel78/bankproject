
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):


    return   render(request,'index.html')

def login(request):
    if request.method =='POST':
        username=request.POST.get('username','')

        password = request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:single')
        else:

            return redirect('bankapp:login')
    return render(request, "login.html", {'message': 'Invalid credentials'})


def register(request):
    if request.method=='POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password1= request.POST.get('password1','')

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('bankapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("User created")
                return redirect('bankapp:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('bankapp:register')

    return render(request, "register.html")
def single(request):


    return   render(request,'single.html')


def form(request):
 if request.method == 'POST':
        messages.success(request,'Application accepted')

 return  render(request,'form.html')
