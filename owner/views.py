from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Owner, Notice
from association.models import Complaint, Expenditure
from django.utils import timezone
# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05":"May", "06": "June", "07": "July", "08":"August", "09": "September","10":"October","11":"November", "12": "December"}

def signup(request):
    if request.method == 'POST':
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
    return render(request, 'owner/signup.html')

def login(request):
    return render(request, 'owner/login.html')
    
def index(request):
    notices = Notice.objects.all().order_by("-id")
    return render(request, 'owner/index.html', {
        "notices": notices,
    })

def post_complaints(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'Post':
            desc = request.POST['complaint_desc']
            Complaint.objects.create(complaint_desc=desc, issued_date = timezone.now())
            return render(request, 'owner/index.html')
        return render(request, 'owner/postcomplaints.html')
    return render(request, 'owner/postcomplaints.html')

def ledger(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'get':
            month = request.POST['month']
            year = request.POST['year']
            expenditures = Expenditure.objects.filter(month__year= year , month__month= month)
            month = months[month]
            return render(request, 'owner/ledger.html', {
                "months":months,
                "month": month,
                "year": year,
                "expenditures": expenditures
            })
        
        return render(request, 'owner/ledger.html')
    return render(request, 'owner/ledger.html',{
        "months":months,
    })