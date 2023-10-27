from .views import job_list
from django.urls import path

urlpatterns = [
    path('', job_list),
]