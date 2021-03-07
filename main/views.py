from django.shortcuts import redirect, render
from django.http import HttpResponse
from main.models import *
from django.template.response import TemplateResponse
from django.urls import reverse


def index(request):
    user = People.objects.all

    return render(request, "Index.html", context={"user": user})
#


def register(request):
    if request.method == "POST":
        form = People()
        form.fname = request.POST.get("fname")
        form.lname = request.POST.get("lname")
        form.email = request.POST.get("email")
        form.mobile = request.POST.get("mobile")
        form.age = request.POST.get("age")
        form.gender = request.POST.get("Gender")
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        f = People.objects.filter(email=form.email).exists()
        print(f)
        if f:
            return TemplateResponse(request, "register.html", {"error": "Email already exist"})

        else:
            print(form)
            if pass1 == pass2:
                form.passwd = pass1
                form.save()
                user = People.objects.get(email=form.email)
                pvtkey = f'{user.Pid}_{user.fname}{user.lname}'
                return redirect('home', pvtkey, user.state)
            else:
                return TemplateResponse(request, "register.html", {'error': "Passowrd Mismatch"})
    else:
        return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        email1 = request.POST.get("email")  # local email variable
        pasw = request.POST.get("pass")  # local password variable
        if People.objects.filter(email=email1).exists():
            user = People.objects.get(email=email1)
            if user.passwd == pasw:
                pvtkey = f'{user.Pid}_{user.fname}{user.lname}'
                return redirect('home', pvtkey, user.state)
            else:
                return TemplateResponse(request, "login.html", {'error': "Passowrd Mismatch"})
        else:
            return TemplateResponse(request, "login.html", {'error': "Email Doesn't Exists"})
    else:
        return render(request, "login.html")


def home(request, Pid, state):
    key = Pid.split('_')
    id = key[0]
    name = key[1]
    user = People.objects.get(Pid=id)
    if name == f'{user.fname}{user.lname}':
        if state == 'Happy':
            user.state = 'Happy'
            user.save()
            ppl = People.objects.filter(state='Sad')
        elif state == 'Sad':
            user.state = 'Sad'
            user.save()
            ppl = People.objects.filter(state='Happy')
        return render(request, 'home.html', {'login': True, 'user': user, 'ppl': ppl})
    else:
        return redirect('login')


def profile(request, Pid):
    key = Pid.split('_')
    id = key[0]
    name = key[1]
    user = People.objects.get(Pid=id)
    pvtkey = f'{user.Pid}_{user.fname}{user.lname}'
    if name == f'{user.fname}{user.lname}':
        if request.method == "POST":

            user.fname = request.POST.get("fname")
            user.lname = request.POST.get("lname")
            user.email = request.POST.get("email")
            user.mobile = request.POST.get("mobile")
            user.age = request.POST.get("age")
            user.gender = request.POST.get("Gender")
            user.bio = request.POST.get("bio")
            print(user.bio)
            user.save()
            return redirect('profile', pvtkey)
        else:
            return render(request, 'profile.html', {'user': user, 'login': True})
    else:
        return redirect('login')


def about(request):
    return render(request, 'about.html')


def changepass(request, Pid):
    key = Pid.split('_')
    id = key[0]
    name = key[1]
    user = People.objects.get(Pid=id)
    pvtkey = f'{user.Pid}_{user.fname}{user.lname}'
    if name == f'{user.fname}{user.lname}':
        if request.method == 'POST':
            opass = request.POST.get('opass')
            npass1 = request.POST.get('npass1')
            npass2 = request.POST.get('npass2')
            if user.passwd == opass:
                if npass1 == npass2:
                    user.passwd = npass1
                    user.save()
                    return render(request, 'changepass.html', {'login': True, 'user': user, 'error': "Password Changed Successfully"})
                else:
                    return render(request, 'changepass.html', {'login': True, 'user': user, 'error': "New Password Mismatched"})
            else:
                return render(request, 'changepass.html', {'login': True, 'user': user, 'error': "Incorrect Old Password"})
        else:
            return render(request, 'changepass.html', {'login': True, 'user': user})
    else:
        return redirect('login')
