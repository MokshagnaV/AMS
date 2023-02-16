from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

class signup(View):
    def post(self, request):
        pass
    def get(self, request):
        return render(request, 'owner/signup.html')