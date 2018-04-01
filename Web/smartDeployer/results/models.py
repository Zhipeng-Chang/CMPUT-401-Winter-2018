from django.db import models

# Create your models here.

class WorkloadA(models.Model):
    exp = models.TextField()
    avgThroughput = models.FloatField()
    avgReadLatency = models.FloatField()
    avgWriteLatency = models.FloatField()

class WorkloadB(models.Model):
    expID = models.IntegerField()
    workload = models.IntegerField()
    latency = models.FloatField()

class WorkloadC(models.Model):
    expID = models.IntegerField()
    workload = models.IntegerField()
    latency = models.FloatField()

class WorkloadD(models.Model):
    expID = models.IntegerField()
    workload = models.IntegerField()
    latency = models.FloatField()

class Experiments(models.Model):
    expID = models.IntegerField()
    cpus = models.IntegerField()
    ram = models.IntegerField()
    io = models.IntegerField()
