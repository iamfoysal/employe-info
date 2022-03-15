from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import CustomRegisterFrom





def register(request):
    login_form = CustomRegisterFrom()

    if request.method == 'POST':
        login_form = CustomRegisterFrom(request.POST)

        if login_form.is_valid():
            login_form.save()
            return redirect ("login")
    return render (request,"useraccess/register.html", {"login_form": login_form})


    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
           
    return render(request, "useraccess/login.html")


def logout(request):
    logout(request)
    return redirect("login")