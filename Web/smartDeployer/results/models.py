from django.db import models

# Create your models here.

class WorkloadA(models.Model):
    exp = models.TextField()
    avgThroughput = models.FloatField()
e    avgReadLatency = models.FloatField()
    avgWriteLatency = models.FloatField()

class WorkloadB(models.Model):
    exp = models.TextField()
    avgThroughput = models.FloatField()
    avgReadLatency = models.FloatField()
    avgWriteLatency = models.FloatField()

class WorkloadC(models.Model):
    exp = models.TextField()
    avgThroughput = models.FloatField()
    avgReadLatency = models.FloatField()

class WorkloadD(models.Model):
    exp = models.TextField()
    avgThroughput = models.FloatField()
    avgReadLatency = models.FloatField()
    avgInsertLatency = models.FloatField()

class Experiments(models.Model):
    expID = models.IntegerField()
    cpus = models.IntegerField()
    ram = models.IntegerField()
    io = models.IntegerField()
