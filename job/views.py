from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import  CreateView
from django.db.models import Q , F        #Q: to use the OR condition in filter conditions ^ F: i use it so i can do comparisions between 2 columns
from django.db.models.aggregates import Count , Sum , Min , Max , Avg  
from django.views.decorators.cache import cache_page
from .forms import JobApplyForm , JobForm
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
    form_class = JobApplyForm
    

    def form_valid(self,form):
        slug = self.kwargs.get('slug')
        job = get_object_or_404(Job, slug=slug)
        job_apply= form.save(commit=False)
        job_apply.job = job
        job_apply.save()
        return super().form_valid(form)

@cache_page(60 * 1)
def mydebug(request):
                                                            # FILTER OBJECTS:     !!
    # data = job.objects.filter(experience__gt=5)            * filter jobs where experience > 5 *
    # data = job.objects.filter(experience__gte=5)           * filter jobs where experience >= 5 *
    # data = job.objects.filter(experience__lt=5)            * filter jobs where experience < 5 *
    # data = job.objects.filter(experience__lte=5)           * filter jobs where experience <= 5 *
    # data = job.objects.filter(experience__range=(1,3)      * filter jobs where experience = 1,2,3 *
    # data = job.objects.filter(company__id=5)               * filter jobs where company number is 5 *
    # data = job.objects.filter(company__id__gt=5)           * filter jobs where company number > 5 *
    # data = job.objects.filter(title__contains='python')    * filter jobs which have the word python in their title *
    # data = job.objects.filter(title__startswith='python')  * filter jobs which their title starts with word python *
    # data = job.objects.filter(title__endswith='needed')    * filter jobs which their title ends with word needed *
    # data = job.objects.filter(salary_start__isnull=True)   * filter jobs which their salary is hidden (no salary given) *
    # data = job.objects.filter(created_at__year=2023)       * filter all jobs was created at year 2023 *
    # data = job.objects.filter(created_at__month=10)        * filter all jobs was created at month 10 *
    # data = job.objects.filter(created_at__date='2023-10-05')* filter all jobs was created at the date '2023-10-05' *
    # data = job.objects.filter(salary_start__gt=1000 , experience__gt=5)         * filter jobs with 2 conditions (and) *
    # data = job.objects.filter(
    # Q(salary_start__gt=1000) | Q(experience__gt=5)
    # )   * filter jobs with 2 conditions (OR) *
    # data = job.objects.filter(
    # Q(salary_start__gt=1000) & ~Q(experience__gt=5)
    # )   * filter jobs with 2 conditions (AND NOT) *
    # data = job.objects.filter(salary_start=F('salary_end'))        * filter jobs with where salary_start = salary_end same price*          'F'
    # data = Job.objects.all().order_by('experience')                * filter jobs by their experience from the lowest to the highest experience
    # data = Job.objects.all().order_by('-experience')               * filter jobs by their experience from the highest to the lowest experience
    # data = Job.objects.all()[:5] *will display first 5 jobs
    # data = Job.objects.all()[5:10] *will display from job number 5 to job number 10
    # data = Job.objects.values('id','title') *will display all jobs ids & titles only         *Dictionary*
    # data = Job.objects.values_list('id','title') *will display all jobs ids & titles only         *tuples*
    # data = Job.objects.values('id','title').distinct() *will display all jobs ids & titles only without repeatation         *Dictionary*
    # data = Job.objects.defer('category') *will display all jobs without category column
    # data = Job.objects.aggregate(Sum('experience')) *will display the sum result of all job experiences
    # data = Job.objects.aggregate(my_sum=Sum('experience') , min_salary_end=Min('salary_end')) *will display the sum result of all job experiences and minimum salary end value
    # data = Job.objects.annotate(salary_with_tax = F('salary_start')*1.15)  *will be displayed only in the sql debug page sel action as a temporary column
    data = Job.objects.only('id','title')
    return render(request, 'job/debug.html', {'data':data})

def about_view(request):
    return render(request, 'job/about.html', {})

def contact_view(request):
    return render(request, 'job/contact.html', {})

class AddJob(CreateView):
    model = Job
    #fields = ['title','location','company','salary_start','salary_end','description','vacancy','job_type','experience','category']
    form_class = JobForm
    success_url = '/jobs/'