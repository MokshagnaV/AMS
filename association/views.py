from django.shortcuts import render, redirect
from owner.models import Notice
from .models import Complaint, Expenditure
from django.urls import reverse
import datetime
# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05":"May", "06": "June", "07": "July", "08":"August", "09": "September","10":"October","11":"November", "12": "December"}

def notice_add(request):
    if request.method == 'POST':
        form = request.POST['notices']
        if form == 'Add':
            notice_title = request.POST['notice-title']
            desc = request.POST['desc']
            Notice.objects.create(notice_title=notice_title, notice_desc=desc)
            return render(request, 'association/index.html')
        return render(request, 'association/noticesadd.html')
    
    return render(request, 'association/noticesadd.html')

def index(request):
    return render(request, 'association/index.html')

def complaints(request):
    complaints = Complaint.objects.all().order_by('-id')
    return render(request, 'association/complaints.html', {
        "complaints": complaints 
    })

def ledger(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'get':
            month = request.POST['month']
            year = request.POST['year']
            expenditures = Expenditure.objects.filter(month__year= year , month__month= month)
            month = months[month]
            return render(request, 'association/ledger.html', {
                "months":months,
                "month": month,
                "year": year,
                "expenditures": expenditures
            })
        
        return redirect('association-ledger')
    
    today = datetime.date.today()

    year = today.year
    month = "{:02d}".format(today.month - 1)
    if(month == 12):
        year -= 1

    expenditures = Expenditure.objects.filter(month__year= year , month__month= month)

    return render(request, 'association/ledger.html',{
        "months":months,
        "month": months[month],
        "year": year,
        "expenditures": expenditures
    }) 

def addexpense(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'submit':
            date = request.POST['date']
            try:
                for i in range(1, 100):    
                    expense = request.POST[f'expense{i}']
                    amount = request.POST[f'amount{i}']
                    Expenditure.objects.create(month=date, item=expense, amount=amount)
            except(Exception):
                pass
            return redirect(reverse('ledger'))
        return render(request, 'association/addexpense.html')
    return render(request, 'association/addexpense.html')