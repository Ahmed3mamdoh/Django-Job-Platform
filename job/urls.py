from .views import job_list , job_details
from django.urls import path
from .api import job_list_api , job_detail_api


urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_details),
    path('api/list' , job_list_api),
    path('api/list/<int:id>' , job_detail_api),
]