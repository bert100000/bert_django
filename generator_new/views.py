from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def password(request):
    return render(request,'./password.html',{'password':123456})


def index(request):
    print('hello man')
    

    return render(request,'./index.html',{'password':123456}) 