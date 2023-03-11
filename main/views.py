from django.shortcuts import render, redirect
from django.views import View
from .models import Owner, Association, OwnerProfile, AssociationProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
# Create your views here.

def index(request):
        return render(request, 'main/index.html')
    
def owner_login(request):
    if request.method == 'POST':
        print('HELLOO OWNER')
        form = request.POST['owner']
        if form == 'Login':
            username = request.POST['owner-username']
            password = request.POST['owner-password']

            details = Owner.objects.get(role = 'Owner', username = username)

            if details.role == 'OWNER':
                user= authenticate(request, username=username, password=password)

                if user is not None:
                    request.session['uname']=username
                    auth_login(request, user)
                    return redirect('owner-home')
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return render(request, "main/login.html")
    return redirect('main-login')
    

def association_login(request):
    if request.method == 'POST':
        form = request.POST['association']
        if form == 'Login':
            username = request.POST['assocation-username']
            password = request.POST['assocation-password']

            details = Association.objects.get(role = 'Association', username = username)
            if details.role == 'ASSOCIATION':
                user= authenticate(request, username=username, password=password)

                if user is not None:
                    request.session['uname']=username
                    auth_login(request, user)
                    return redirect('association-home')
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return render(request, "main/login.html")
    return redirect('main-login')

def login(request):
    return render(request, 'main/login.html')
    
def signup(request):
    if request.method == 'POST':
        form=request.POST['submit']
        if form=='Submit':
            username = request.POST['username']
            password = request.POST['pass']
            usertype = request.POST['user_type']
            email = request.POST['email']
            name = request.POST['fname']
            phnum = request.POST['phnumber']
            
            if usertype == 'Owner' :
                Owner.objects.create_user(username = username, password = password)
                user = OwnerProfile.objects.get(user = Owner.objects.get(username = username))
                user.OwnerName = name
                user.email = email
                user.OwnerPhNo = phnum
                user.save()
                return redirect('main-login')

            elif usertype == 'Association':
                Association.objects.create_user(username = username, password = password)
                user = AssociationProfile.objects.get(user = Association.objects.get(username = username))
                user.AssociationName = name
                user.email = email
                user.AssociationPhNo = phnum
                user.save()
                return redirect('main-login')

                
    return render(request, "main/signup.html")
    
def logoutUser(request):
    # del request.session['uname']  
    logout(request)
    #messages.info(request, 'Logout successful')
    return redirect('main')