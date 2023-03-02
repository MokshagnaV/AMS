from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import Owner, Notice
from association.models import Complaint, Expenditure
from django.utils import timezone
import datetime

# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05":"May", "06": "June", "07": "July", "08":"August", "09": "September","10":"October","11":"November", "12": "December"}

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
            return redirect('owner-home')
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
        
        return redirect('owner-ledger')
    
    today = datetime.date.today()

    year = today.year
    month = "{:02d}".format(today.month - 1)
    if(month == 12):
        year -= 1

    expenditures = Expenditure.objects.filter(month__year= year , month__month= month)

    return render(request, 'owner/ledger.html',{
        "months":months,
        "month": months[month],
        "year": year,
        "expenditures": expenditures
    }) 