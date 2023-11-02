from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Job
# Create your views here.


def job_list(request):
    all_jobs = Job.objects.all()
    jobs_count = all_jobs.count()

    page = request.GET.get('page', 1)

    paginator = Paginator(all_jobs, 50)
    try:
        all_jobs = paginator.page(page)
    except PageNotAnInteger:
        all_jobs = paginator.page(1)
    except EmptyPage:
        all_jobs = paginator.page(paginator.num_pages)
    return render (request, 'job/job_list.html',{'jobs':all_jobs,'jobs_count':jobs_count})


def job_details(request , slug):
    job = Job.objects.get(slug=slug)
    return render (request, 'job/job_details.html',{'job':job})

