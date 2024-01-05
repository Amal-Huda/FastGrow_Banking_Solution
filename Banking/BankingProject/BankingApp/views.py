from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Districts, Branches, Customer
from .forms import Customerform


# Create your views here.
def Home(request):
    return render(request, 'index.html')


def Login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['pword']
        user = auth.authenticate(username=uname, password=pword)
        print(user.is_authenticated, user.username)

        if request.user is not None:
            auth.login(request, user)
            print(" username", user.username)
            return redirect('/')
            # print(user.is_authenticated, request.user.is_authenticated)
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('BankingApp:login')

    return render(request, 'Login.html', {'request': request})


# def Register(request):
#     if request.method == 'POST':
#         uname = request.POST['username']
#         pword = request.POST['pword']
#         cpword = request.POST['cpword']
#         if pword == cpword:
#             if User.objects.filter(username=uname).exists():
#                 messages.info(request, 'username already exists')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=uname, password=pword)
#                 user.save()
#                 print("user created")
#             return redirect('login')
#         else:
#             messages.info(request, 'Password not matching')
#             print("password not match")
#             return redirect('register')
#         return redirect('/')
#     return render(request,'Register.html')
def Register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['pword']
        cpword = request.POST['cpword']
        if pword == cpword:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'username already exists')
                # return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=pword)
                user.save()
                return redirect('BankingApp:login')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('BankingApp:register')
        return redirect('/')
    return render(request, 'Register.html')


def Apply(request):
    distobj = Districts.objects.all()
    branches=Branches.objects.all()
    form = Customerform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('BankingApp:applicationsuccess')
    else:
        form=Customerform()
    return render(request, 'ApplyNetBanking.html', dict(form=form,districts=distobj, branches=branches))





def ApplicationSuccess(request):
    message = 'Application Submitted succesfully..'
    return render(request, 'ApplicationAccept.html', {'message': message})



#
#         customer=Customer(name=name,age=age,phone=phone)
#         distobj=Districts.objects.all().filter(district==district)
#         branch = request.POST.get('branch')
#         brncobj=Branches.objects.all().filter(branch==branch)
#         customer.save()
#         distobj.save()
#         brncobj.save()
#     return render(request,'ApplyNetBanking.html',{'customer':customer,'district':distobj,'branch':brncobj})
#
#

def Logout(request):
    auth.logout(request)
    return redirect('/')
