from django.shortcuts import render, redirect
from owner.models import Notice
from .models import Complaint, Expenditure, Payment, BankBalance
from django.urls import reverse
from main.models import Association, AssociationProfile
from django.db.models import Sum
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required
import os
# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05":"May", "06": "June", "07": "July", "08":"August", "09": "September","10":"October","11":"November", "12": "December"}

@login_required(login_url='main')
def index(request):
    userName = AssociationProfile.objects.get(user = request.user)
    return render(request, 'association/index.html', {
        "user": userName
    })

@login_required(login_url='main')
def notice_add(request):
    username = AssociationProfile.objects.get(user = request.user)

    if request.method == 'POST':
        form = request.POST['notices']
        if form == 'Add':
            notice_title = request.POST['notice-title']
            desc = request.POST['desc']
            user = Association.objects.get(username = request.user)
            username = AssociationProfile.objects.get(user = user)
            Notice.objects.create(notice_by=user,notice_title=notice_title, notice_desc=desc)
            return redirect('association-home')
        return redirect('notices_add')
    
    return render(request, 'association/noticesadd.html', {
        "user": username
    })

@login_required(login_url='main')
def complaints(request):
    complaints = Complaint.objects.all().order_by('-id')
    username = AssociationProfile.objects.get(user = request.user)
    return render(request, 'association/complaints.html', {
        "complaints": complaints ,
        "user": username
    })

@login_required(login_url='main')
def ledger(request):
    username = AssociationProfile.objects.get(user = request.user)

    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'get':
            month = request.POST['month']
            year = request.POST['year']
            expenditures = Expenditure.objects.filter(month__year= year , month__month= month)
            totalExpenditure = expenditures.aggregate(Sum('amount'))
            try:
                opening_balance = BankBalance.objects.get(month__month = int(month) - 1, month__year = year).balance
            except:
                opening_balance = False
            maintenace = Payment.objects.filter(payment_for = 'MB', payment_date__year= year , payment_date__month= month).aggregate(Sum('amount'))
            function_hall = Payment.objects.filter(payment_for = 'FH', payment_date__year= year , payment_date__month= month).aggregate(Sum('amount'))
            others = Payment.objects.filter(payment_for = 'OB', payment_date__year= year , payment_date__month= month).aggregate(Sum('amount'))
            month = months[month]
            return render(request, 'association/ledger.html', {
                "months":months,
                "month": month,
                "year": year,
                "expenditures": expenditures,
                "open_bal": opening_balance,
                "maintenance": maintenace,
                "function_hall": function_hall,
                "other": others,
                "expenditure": totalExpenditure,
            })
        
        return redirect('association-ledger')
    
    today = datetime.date.today()

    year = today.year
    month = "{:02d}".format(today.month - 1)
    if(month == 12):
        year -= 1

    expenditures = Expenditure.objects.filter(month__year= year , month__month= month)
    totalExpenditure = expenditures.aggregate(Sum('amount'))
    try:
        opening_balance = BankBalance.objects.get(month__month = int(month) - 1, month__year = year).balance
    except:
        opening_balance = False
    maintenace = Payment.objects.filter(payment_for = 'MB', payment_date__year= year , payment_date__month= month).aggregate(Sum('amount'))
    return render(request, 'association/ledger.html',{
        "months":months,
        "month": months[month],
        "year": year,
        "expenditures": expenditures,
        "open_bal": opening_balance,
        "maintenance": maintenace,
        "expenditure": totalExpenditure,
        "user": username
    }) 

@login_required(login_url='main')
def addexpense(request):
    username = AssociationProfile.objects.get(user = request.user)

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
            return redirect(reverse('association-ledger'))
        return redirect('addexpense')
    return render(request, 'association/addexpense.html', {
        "user": username
    })

@login_required(login_url='main')
def payments(request):
    username = AssociationProfile.objects.get(user = request.user)

    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'get':
            month = request.POST['month']
            year = request.POST['year']
            month_payments = Payment.objects.filter(payment_date__year= year , payment_date__month= month)
            month = months[month]
            return render(request, 'association/payments.html', {
                "months":months,
                "month": month,
                "year": year,
                "month_payments": month_payments
            })
        return redirect('payments')    

    payments = Payment.objects.all()
    return render(request, 'association/payments.html',{
        "months":months,
        "payments": payments,
        "user": username
    })

@login_required(login_url='main')
def complaint_resolve(request, id):

    complaint = Complaint.objects.filter(id = id)
    complaint.update(resolved_date = timezone.now()) 

    return redirect('complaints')

@login_required(login_url='main')
def profile(request):
    user = AssociationProfile.objects.get(user = request.user)
    return render(request, 'association/profile.html', {
        "user": user,
    })

@login_required(login_url='main')
def editprofile(request):
    user = AssociationProfile.objects.get(user = request.user)

    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'Done':
            name = request.POST['name']
            email = request.POST['email']
            phno = request.POST['phone-num']
            role = request.POST['role']
            try:
                dp = request.FILES['profile-pic']       
                if user.ProfilePic != '':
                    os.remove(user.ProfilePic.path)
                    user.ProfilePic = dp
                else:
                    user.ProfilePic = dp
            except:
                pass
            user.email = email
            user.AssociationName = name
            user.AssociationPhNo = phno
            user.AssociationRole = role
            user.save()
            return redirect('association-profile')

    return render(request, 'association/editprofile.html', {
        "user": user,
    })