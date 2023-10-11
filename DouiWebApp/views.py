from django.shortcuts import render

# Create your views here.


def showDemoPage(request):
    return render(request, "index.html")


def loginPage(request):
    return render(request, "login.html")


def profilePage(request):
    return render(request, "profile.html")


def registerPage(request):
    return render(request, "register.html")


def tablePage(request):
    return render(request, "table.html")

