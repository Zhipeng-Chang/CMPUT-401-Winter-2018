from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkloadA, WorkloadB, WorkloadC, WorkloadD, Experiments

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart




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

def workloada(request):
    num_elements = WorkloadA.objects.all().count()
    

#    return render(request, 'workloada.html',context={})

    data =  [
        ['Year', 'Sales', 'Expenses'],
        [2004, 1000, 400],
        [2005, 1170, 460],
        [2006, 660, 1120],
        [2007, 1030, 540]
        ]
    # DataSource object
    data_source = SimpleDataSource(data=data)
    # Chart object
    chart = LineChart(data_source)
    context = {'chart': chart}
    return render(request, 'workloada.html', context)





def workloadb(request):
	return render(request, 'workloadb.html',context={})

def workloadc(request):
	return render(request, 'workloadc.html',context={})

def workloadd(request):
	return render(request, 'workloadd.html',context={})
