from .views import job_list , job_details , JobApply
from django.urls import path
from .api import JobListAPI , JobDetailAPI


urlpatterns = [
    path('', job_list),
    path('<slug:slug>', job_details),
    path('<slug:slug>/apply', JobApply.as_view()),
    path('api/list' , JobListAPI.as_view()),
    path('api/list/<int:pk>' , JobDetailAPI.as_view()),
]