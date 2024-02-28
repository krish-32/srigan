from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'admin/admin_login.html')


def admin_page(request):
    if request.method=='POST':
        try:
            mail=request.POST.get('email')
            user=User.objects.filter(email=mail)
            if user and Admin.objects.filter(email=mail):
                messages.success(request,'*Continue to enter the password*')
                return render(request,'admin/admin_login.html',context={'data':mail})

            elif mail != user  and request.POST.get('pass') is None:
                messages.success(request,'*Enter a valid Email*')
                print('a')
                return render(request,'admin/admin_login.html',context={'data':''})
            else:
                pwd=request.POST.get('pass')
                email=request.POST.get('mail')
                e=User.objects.filter(email=email)
                if e:
                    usern=User.objects.get(email=email.lower()).username
                else:
                    usern=''
                user=authenticate(username=usern,password=pwd)
                print(user)
                if user is not None:
                    login(request,user)
                    if request.user.is_authenticated:
                        messages.success(request,'*Login successfully*')
                        return render(request,'admin/admin_home.html')
                else:
                    messages.success(request,'*Mismatch of username or password*')
                    return render(request,'admin/admin_login.html')
        except Exception:
            return render(request,'admin/admin_login.html')
    return render(request,'admin/admin_login.html')