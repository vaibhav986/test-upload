from django.shortcuts import render
from django.http import HttpResponse
def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def process(request):
    print("Welcome")  
    print(request.method)
    print(request.POST)
    fname = (request.POST['fname'])
    lname = (request.POST['lname'])
    mail = (request.POST['email'])
    dob = (request.POST['dob'])
    mobile = (request.POST['mobile'])
    
    return render(request,'ans1.html',{'fname':fname,'lname':lname,'mail':mail,'dob':dob,'mobile':mobile})    