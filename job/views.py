from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import  CreateView
from .models import Job , JobApply
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


class JobApply(CreateView):
    model = JobApply
    success_url = '/jobs/'
    fields = ['username','email','linkedin_profile','github_profile','cv','cover_letter']
    

    def form_valid(self,form):
        slug = self.kwargs.get('slug')
        job = get_object_or_404(Job, slug=slug)
        job_apply= form.save(commit=False)
        job_apply.job = job
        job_apply.save()

        return super().form_valid(form)