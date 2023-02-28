from django.shortcuts import render
from django.views import View

# Create your views here.

class index(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'main/index.html')
    
class login(View):
    def post(self, request):
        form = request.POST['submit']
        if form == 'submit':
            pass
    def get(self, request):
        return render(request, 'main/login.html')