from .views import job_list , job_details
from django.urls import path

urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_details),
]