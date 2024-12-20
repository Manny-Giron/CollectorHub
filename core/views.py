from django.shortcuts import render, HttpResponse

# Create your views here.
def loginPage(request):
    context ={}
    return render(request, "loginPage.html", context)

def home(request):
    return render(request, "frontPage.html" )

def about(request):
    return render(request, "aboutPage.html")