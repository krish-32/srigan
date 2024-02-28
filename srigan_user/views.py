from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def user(request):
    if request.method=='POST':
        mail=request.POST.get('email')
        print(mail)
        if users.objects.filter(email=mail):
            data=users.objects.filter(email=mail)
            print(data)
            return render(request,'user/user_login.html',context={'data':mail})
        if users.objects.filter(password=request.POST.get('pwd')):
                 return render(request,'user/userpage.html')
        else:
            return render(request,'user/user_login.html')
    else:
        return render(request,'user/user_login.html')
