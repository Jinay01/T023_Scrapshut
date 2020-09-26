from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('ngo/<str:pk>/summary/', views.ngo_summary, name='ngo_summary'),
    path('ngo/<str:pk>/tabular/', views.ngo_tabular, name='ngo_tabular'),
    path('ngo/<str:pk>/requirementform/',
         views.ngo_requirementform, name='ngo_requirement'),
]
