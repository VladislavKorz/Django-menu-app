from django.shortcuts import render

def Home(request, URL_Name = None):
    return render(request, "menu/home.html")