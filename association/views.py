from django.shortcuts import render, redirect
from django.views import View
from owner.models import Notice
from .models import Complaint, Expenditure
from django.urls import reverse
# Create your views here.

months = {"01": "January", "02": "February", "03": "March", "04": "April", "05":"May", "06": "June", "07": "July", "08":"August", "09": "September","10":"October","11":"November", "12": "December"}

class notice_add(View):
    def post(self, request):
        form = request.POST['notices']
        if form == 'Add':
            notice_title = request.POST['notice-title']
            desc = request.POST['desc']
            Notice.objects.create(notice_title=notice_title, notice_desc=desc)
            return render(request, 'association/index.html')
        return render(request, 'association/noticesadd.html')
        
    def get(self, request):
        return render(request, 'association/noticesadd.html')

class index(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'association/index.html')

class complaints(View):
    def post(slef, request):
        pass
    def get(self, request):
        complaints = Complaint.objects.all().order_by('-id')
        return render(request, 'association/complaints.html', {
            "complaints": complaints 
        })

class ledger(View):
    def post(slef, request):
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
        
        return render(request, 'association/ledger.html')
    def get(self, request):        
        return render(request, 'association/ledger.html',{
            "months":months,
        })

class addexpense(View):
    def post(self, request):
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
    def get(self, request):
        return render(request, 'association/addexpense.html')