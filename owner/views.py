from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import Notice
from association.models import Complaint, Expenditure, Payment, BankBalance
from main.models import Owner, Association
from django.db.models import Sum
from django.utils import timezone
import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
          "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

@login_required(login_url='main')
def index(request):
    notices = Notice.objects.all().order_by("-id")
    user = Owner.objects.get(username=request.session.get('uname'))
    complaints = Complaint.objects.filter(complaint_by=user)
    return render(request, 'owner/index.html', {
        "notices": notices,
        "complaints": complaints,
    })


@login_required(login_url='main')
def post_complaints(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'Post':
            desc = request.POST['complaint_desc']
            user = Owner.objects.get(username=request.session.get('uname'))
            Complaint.objects.create(
                complaint_by=user, complaint_desc=desc, issued_date=timezone.now())
            return redirect('owner-home')
        return render(request, 'owner/postcomplaints.html')
    return render(request, 'owner/postcomplaints.html')


@login_required(login_url='main')
def ledger(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'get':
            month = request.POST['month']
            year = request.POST['year']
            expenditures = Expenditure.objects.filter(
                month__year=year, month__month=month)

            totalExpenditure = expenditures.aggregate(Sum('amount'))
            try:
                opening_balance = BankBalance.objects.get(
                    month__month=int(month) - 1, month__year=year).balance
            except:
                opening_balance = False
            maintenace = Payment.objects.filter(
                payment_for='MB', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))
            function_hall = Payment.objects.filter(
                payment_for='FH', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))
            others = Payment.objects.filter(
                payment_for='OB', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))

            month = months[month]
            return render(request, 'owner/ledger.html', {
                "months": months,
                "month": month,
                "year": year,
                "expenditures": expenditures,
                "open_bal": opening_balance,
                "maintenance": maintenace,
                "function_hall": function_hall,
                "other": others,
                "expenditure": totalExpenditure,
            })

        return redirect('owner-ledger')

    today = datetime.date.today()

    year = today.year
    month = "{:02d}".format(today.month - 1)
    if (month == 12):
        year -= 1

    expenditures = Expenditure.objects.filter(
        month__year=year, month__month=month)

    totalExpenditure = expenditures.aggregate(Sum('amount'))
    try:
        opening_balance = BankBalance.objects.get(
            month__month=int(month) - 1, month__year=year).balance
    except:
        opening_balance = False
    maintenace = Payment.objects.filter(
        payment_for='MB', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))
    function_hall = Payment.objects.filter(
        payment_for='FH', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))
    others = Payment.objects.filter(
        payment_for='OB', payment_date__year=year, payment_date__month=month).aggregate(Sum('amount'))
    return render(request, 'owner/ledger.html', {
        "months": months,
        "month": months[month],
        "year": year,
        "expenditures": expenditures,
        "open_bal": opening_balance,
        "maintenance": maintenace,
        "function_hall": function_hall,
        "other": others,
        "expenditure": totalExpenditure,
    })


@login_required(login_url='main')
def make_payment(request):
    if request.method == 'POST':
        form = request.POST['submit']
        if form == 'Done':
            amount = request.POST['amount']
            payment_mode = request.POST['payment_mode']
            payment_desc = request.POST['payment_desc']
            utr = request.POST['utr']
            reciept_no = request.POST['reciept_no']
            pay_for = request.POST['pay_for']
            user = Owner.objects.get(username=request.session.get('uname'))

            Payment.objects.create(user=user, reciept_no=reciept_no, payment_desc=payment_desc,
                                   payment_mode=payment_mode, UTR=utr, payment_date=timezone.now(), amount=amount, payment_for=pay_for)
            return redirect('owner-home')
        return render(request, 'owner/makepayment.html')

    return render(request, 'owner/makepayment.html')
