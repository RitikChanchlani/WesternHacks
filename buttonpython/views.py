from django.shortcuts import render
import requests
import sys

from subprocess import run,PIPE
def button(request):
    return render(request,'home.html')

def home(request):
    return render(request,'hello.html')

def translator(request):
    return render(request, 'translator.html')

def educational(request):
    return render(request,'educational.html')

def about(request):
    return render(request,'about.html')

def external(request):
    imp=request.POST.get('param')
    print (imp)
    out=run([sys.executable,'\\Users\\chanc\\OneDrive\\Documents\\WesternHacks\\Detector.py',imp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'translator.html',{'data1':out.stdout.decode('utf-8')})

def website(request):
    imp=request.POST.get('website')
    print (imp)
    out=run([sys.executable,'\\Users\\chanc\\OneDrive\\Documents\\WesternHacks\\WebpageDetector.py',imp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'translator.html',{'data2':out.stdout.decode('utf-8')})