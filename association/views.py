from django.shortcuts import render
from django.views import View
from owner.models import Notice
# Create your views here.

class notice_add(View):
    def post(self, request):
        form = request.POST['submit']
        if form == 'Submit':
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

