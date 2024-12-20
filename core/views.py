from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
            
    user = authenticate(request, username=username, password=password)    

    if user is not None:
        login(request, user)
        return render(request, "frontPage.html")
    else:
        messages.error(request, "Username or password does not exist")
            

    context ={}
    return render(request, "loginPage.html", context)

def home(request):
    return render(request, "frontPage.html" )

def about(request):
    return render(request, "aboutPage.html")