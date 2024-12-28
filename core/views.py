from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:  # Specify the exception type
            messages.error(request, "User does not exist")
            return render(request, "loginPage.html")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)    

        if user is not None:
            login(request, user)
            return redirect("home")  # Redirect to the home page (update with your URL name)
        else:
            messages.error(request, "Username or password is incorrect")

    # Render the login page for GET requests or failed POST requests
    context = {'page': page}
    return render(request, "loginPage.html", context)


def registerPage(request):
    page = "register"
    return render(request, "loginPage.html")

def home(request):
    return render(request, "frontPage.html" )

def about(request):
    return render(request, "aboutPage.html")