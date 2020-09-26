from django.urls import path, include
from . import views
from rest_framework import routers

# url

urlpatterns = [
    # ngo section
    path('ngo', views.ngo, name='ngo'),

    # donor section
    path('donor', views.donor, name='donor'),

]
