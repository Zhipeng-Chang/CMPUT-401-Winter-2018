from django.urls import path


from . import views
# This two if you want to enable the Django Admin: (recommended)
from django.contrib import admin
admin.autodiscover()


urlpatterns =[
	path('', views.index, name='index'),
	path('team/', views.team, name='team'),
	path('help/', views.help, name='help'),
	path('about/', views.about, name='about')
]
