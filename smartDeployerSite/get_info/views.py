from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
# 	return HttpResponse("hello world!")

#return the html template
def index(request):
	return render('request','get_info/index.html')

def signin(request):
	return render('request','get_info/sign.html')