from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkloadA, WorkloadB, WorkloadC, WorkloadD, Experiments

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
from graphos.sources.model import ModelDataSource



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
    data = WorkloadA.objects.all()
    
    # DataSource object
    data_source = ModelDataSource(data, ['workload', 'latency'])

    # Chart object
    chart = LineChart(data_source, options={'title': 'Workload A'})
    context = {'chart': chart}
    return render(request, 'workloada.html', context)

def workloadb(request):
    data = WorkloadB.objects.all()

    # DataSource object                                                                                                
    data_source = ModelDataSource(data, ['workload', 'latency'])

    # Chart object                                                                                                    
    chart = LineChart(data_source, options={'title': 'Workload B'})
    context = {'chart': chart}
    return render(request, 'workloadb.html', context)

def workloadc(request):
    data = WorkloadC.objects.all()

    # DataSource object                                                                                               
    data_source = ModelDataSource(data, ['workload', 'latency'])

    # Chart object                                                                                                  
    chart = LineChart(data_source, options={'title': 'Workload C'})
    context = {'chart': chart}
    return render(request, 'workloadc.html', context)

def workloadd(request):
    data = WorkloadD.objects.all()

    # DataSource object                                                                                           
    data_source = ModelDataSource(data, ['workload', 'latency'])

    # Chart object                                                                                                 
    chart = LineChart(data_source, options={'title': 'Workload D'})
    context = {'chart': chart}
    return render(request, 'workloadd.html', context)
