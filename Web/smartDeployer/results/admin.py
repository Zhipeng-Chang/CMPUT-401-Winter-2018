from django.contrib import admin

# Register your models here.
from .models import WorkloadA, WorkloadB, WorkloadC, WorkloadD, Experiments

admin.site.register(WorkloadA)
admin.site.register(WorkloadB)
admin.site.register(WorkloadC)
admin.site.register(WorkloadD)
admin.site.register(Experiments)
