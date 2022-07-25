from django.shortcuts import render
from django.http import HttpResponse
def homepageview(request):
    return HttpResponse("<h1>Welcome To DJANGO!!</h1>")

def aboutpageview(request):
    return HttpResponse("<h1>Welcome To ABOUT US page!!</h1>")

def contactpageview(request):
    return HttpResponse("<h1>Welcome To CONTACT US page!!</h1>")
