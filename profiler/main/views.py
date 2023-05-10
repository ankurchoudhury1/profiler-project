from django.shortcuts import render
import hashlib
from . models import Accountusers

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def signup(request):

    if request.method == 'POST':
        USERNAME = request.POST['username']
        EMAIL = request.POST['email']
        PASSWORD = request.POST['password']

        PASSWORD = hashlib.sha256(PASSWORD.encode()).hexdigest()

        q = Accountusers(username=USERNAME, email=EMAIL, password=PASSWORD)

        q.save()


        print(USERNAME, EMAIL, PASSWORD)
        

    return render(request, 'main/signup.html')

def signin(request):

    if request.method == 'POST':
        USERNAME = request.POST['username']
        PASSWORD = request.POST['password']

        print(USERNAME, PASSWORD)
        
    return render(request, 'main/signin.html')

def profile(request):
    return render(request, 'main/profile.html')

def settings(request):
    return render(request, 'main/settings.html')

def blogs(request):
    return render(request, 'main/blogs.html')

def createapost(request):
    return render(request, 'main/createapost.html')

def signout(request):
    pass