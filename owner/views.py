from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Owner, Notice
from association.models import Complaint
from django.utils import timezone
# Create your views here.

class signup(View):
    def post(self, request):
        form = request.POST['submit']
        if form == 'Submit':
            name_ = request.POST['fname'] + " " +request.POST['lname']
            email_ = request.POST['email']
            contact_ = request.POST['phnumber']
            password_ = request.POST['pass']
            confpassword = request.POST['confpas']
            flatno = request.POST['flatno']
            floorno = request.POST['floorno']

            if password_!= confpassword:
                return render(request, 'owner/signup.html')

            owner_details = Owner(
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
    
class index(View):
    def post(self, request):
        pass
    def get(self, request):
        notices = Notice.objects.all().order_by("-id")
        return render(request, 'owner/index.html', {
            "notices": notices,
        })

class post_complaints(View):
    def post(self, request):
        form = request.POST['submit']
        if form == 'Post':
            desc = request.POST['complaint_desc']
            Complaint.objects.create(complaint_desc=desc, issued_date = timezone.now())
            return render(request, 'owner/index.html')
        return render(request, 'owner/postcomplaints.html')

    def get(self, request):
        return render(request, 'owner/postcomplaints.html')