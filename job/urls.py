from .views import job_list , job_details , JobApply , AddJob , about_view , contact_view
from django.urls import path
from .api import JobListAPI , JobDetailAPI


urlpatterns = [
    path('', job_list),
    path('add/', AddJob.as_view()),
    path('<slug:slug>', job_details),
    path('<slug:slug>/apply', JobApply.as_view()),
    path('api/list' , JobListAPI.as_view()),
    path('api/list/<int:pk>' , JobDetailAPI.as_view()),
    path('about/', about_view),
    path('contact/', contact_view),
]