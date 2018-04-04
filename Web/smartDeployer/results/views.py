from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import WorkloadA, WorkloadB, WorkloadC, WorkloadD, Experiments

from graphos.renderers.gchart import ColumnChart
from graphos.sources.model import ModelDataSource


# Create your views here.

def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'home_page.html',context={})

def team(request):
    return render(request, 'team.html',context={})

def help(request):
    return render(request, 'help.html',context={})

def about(request):
    return render(request, 'about.html',context={})

def workloada(request):
    data = WorkloadA.objects.all()
    
    # DataSource object
    data_source = ModelDataSource(data, ['exp', 'avgReadLatency', 'avgWriteLatency', 'avgThroughput'])

    classicOptions = {
        'series': {
            0: {'targetAxisIndex': 0},
            1: {'targetAxisIndex': 0},
            2: {'targetAxisIndex': 1}
            },
        'title': 'Workload A - Average latency on the left, Average throughput on the right',
        'vAxes': {
               0: {'title': 'AVG LATENCY'},
               1: {'title': 'AVG THROUGHPUT'}
               }
        }


    # Chart object
    chart = ColumnChart(data_source, options=classicOptions)
    context = {'chart': chart}
    return render(request, 'workloada.html', context)

def workloadb(request):
    data = WorkloadB.objects.all()

    # DataSource object
    data_source = ModelDataSource(data, ['exp', 'avgReadLatency', 'avgWriteLatency', 'avgThroughput'])

    classicOptions = {
        'series': {
            0: {'targetAxisIndex': 0},
            1: {'targetAxisIndex': 0},
            2: {'targetAxisIndex': 1}
            },
        'title': 'Workload B - Average latency on the left, Average throughput on the right',
        'vAxes': {
            0: {'title': 'AVG LATENCY'},
            1: {'title': 'AVG THROUGHPUT'}
            }
        }

    # Chart Object
    chart = ColumnChart(data_source, options=classicOptions)
    context = {'chart': chart}
    return render(request, 'workloadb.html', context)

def workloadc(request):
    data = WorkloadC.objects.all()

    # DataSource object
    data_source = ModelDataSource(data, ['exp', 'avgReadLatency', 'avgThroughput'])

    classicOptions = {
        'series': {
            0: {'targetAxisIndex': 0},
            1: {'targetAxisIndex': 1}
            },
        'title': 'Workload C - Average latency on the left, Average throughput on the right',
        'vAxes': {
            0: {'title': 'AVG LATENCY'},
            1: {'title': 'AVG THROUGHPUT'}
            }
        }
    
    # Chart object
    chart = ColumnChart(data_source, options=classicOptions)
    context = {'chart': chart}
    return render(request, 'workloadc.html', context)

def workloadd(request):
    data = WorkloadD.objects.all()

    # DataSource object
    data_source = ModelDataSource(data, ['exp', 'avgReadLatency', 'avgInsertLatency', 'avgThroughput'])

    classicOptions = {
        'series': {
            0: {'targetAxisIndex': 0},
            1: {'targetAxisIndex': 0},
            2: {'targetAxisIndex': 1}
            },
        'title': 'Workload D - Average latency on the left, Average throughput on the right',
        'vAxes': {
               0: {'title': 'AVG LATENCY'},
               1: {'title': 'AVG THROUGHPUT'}
               }
        }


    # Chart object
    chart = ColumnChart(data_source, options=classicOptions)
    context = {'chart': chart}
    return render(request, 'workloadd.html', context)
