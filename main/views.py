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
        form = request.POST['submit']
        if form == 'owner':
            username = request.POST['username']
            password = request.POST['password']

            details = Owner.objects.get(role = 'Owner', username = username)

            if details.role == 'CUSTOMER':
                user= authenticate(request, username=username, password=password)

                if user is not None:
                    request.session['uname']=username
                    login(request, user)
                    return redirect('userhome')
                else:
                    messages.info(request, 'Username Or Password is incorrect')
                    return render(request, "main/login.html")
            
    def get(self, request):
        return render(request, 'main/login.html')