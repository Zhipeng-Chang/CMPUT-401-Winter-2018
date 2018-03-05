from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'sample_page.html',context={})

def team(request):
	return render(request, 'team.html',context={})

def help(request):
	return render(request, 'help.html',context={})

def about(request):
	return render(request, 'about.html',context={})