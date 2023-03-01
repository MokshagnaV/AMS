from django.shortcuts import render, redirect
from django.views import View
from .models import Owner, Association
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class index(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'main/index.html')
    
class login(View):
    def post(self, request):
        form = request.POST['owner']
        if form == 'Login':
            username = request.POST['owner-username']
            password = request.POST['owner-password']

            details = Owner.objects.get(role = 'Owner', username = username)

            if details.role == 'OWNER':
                user= authenticate(request, username=username, password=password)

                if user is not None:
                    request.session['uname']=username
                    login(request, user)
                    return redirect('owner-home')
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return render(request, "main/login.html")
    
        form = request.POST['association']
        if form == 'Login':
            username = request.POST['assocation-username']
            password = request.POST['assocation-password']

            details = Association.objects.get(role = 'Association', username = username)

            if details.role == 'ASSOCIATION':
                user= authenticate(request, username=username, password=password)

                if user is not None:
                    request.session['uname']=username
                    login(request, user)
                    return redirect('association-home')
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return render(request, "main/login.html")
            
    def get(self, request):
        return render(request, 'main/login.html')
    
class signup(View):
    def post(self, request):
        form=request.POST['submit']
        if form=='Submit':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['pass']
            usertype = request.POST['user_type']
            
            if usertype == 'Owner' :
                Owner.objects.create_user(username = username, password = password)
                

            elif usertype == 'Association':
                Association.objects.create_user(username = username, password = password)
                

            return render(request, "Book/homepage.html")

    def get(self, request):
        return render(request, 'main/signup.html')