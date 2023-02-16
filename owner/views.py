from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import owner
# Create your views here.

class signup(View):
    def post(self, request):
        form = request.POST['Yes']
        if form == 'Submit':
            name_ = request.POST['fname'] + request.POST['lname']
            email_ = request.POST['email']
            contact_ = request.POST['phnumber']
            password_ = request.POST['pass']
            flatno = request.POST['flatno']
            floorno = request.POST['floorno']
            owner_details = owner(
                password = password_,
                name = name_,
                email = email_,
                contact = contact_,
                flat_no = flatno,   
                floor_no = floorno
            )
            owner_details.save()

            return HttpResponseRedirect("/owner/login")
        return render(request, 'owner/login.html')
    def get(self, request):
        return render(request, 'owner/signup.html')

class login(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'owner/login.html')