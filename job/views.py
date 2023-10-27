from django.shortcuts import render
from .models import Job
# Create your views here.


def job_list(request):
    all_jobs = Job.objects.all()
    return render (request, 'job/job_list.html',{'jobs':all_jobs})


def job_details(request , slug):
    job = Job.objects.get(slug=slug)
    return render (request, 'job/job_details.html',{'job':job})