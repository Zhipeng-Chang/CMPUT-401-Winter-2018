from django.db import models

# Create your models here.

class Scan(models.Model):
    workload = models.IntegerField()
    latency = models.IntegerField()

class Insert(models.Model):
    workload = models.IntegerField()
    latency = models.IntegerField()

class Write(models.Model):
    workload = models.IntegerField()
    latency = models.IntegerField()

class Update(models.Model):
    workload = models.IntegerField()
    latency = models.IntegerField()

class YCSBstats(models.Model):
    cpu = models.IntegerField()
    mem = models.IntegerField()
    io = models.IntegerField()
