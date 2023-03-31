from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def password(request):
    #a-z
    chars=[chr(c) for c in range(97,123)]
    print(chars)
    
    if request.GET.get('uppercase'):
        chars+=[chr(c).upper() for c in range(97,123)]
    
    if request.GET.get('numbers'):
        chars+=list('0123456789')
    
    if request.GET.get('special'):
        chars+=list('@#$%^&*')
    
    

    print(chars)
        
    
    '''input_length=request.GET.get('input-length')
    print(input_length,type(input_length))
    if input_length =='':
        input_length=request.GET.get('length')
        print(input_length)'''
        
    length=eval(request.GET.get('length')) if request.GET.get('input_length')==''\
        else eval(request.GET.get('input_length'))
        
    #random.sample(chars,length)
    password=''.join([random.choice(chars) for i in range(length)])
    print(password)
    #random.choice(chars)
    
        
        
    #print(length)
    return render(request,'./password.html',{'password':password})


def index(request):
    print('hello man')
    

    return render(request,'./index.html') 