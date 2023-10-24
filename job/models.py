from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone




JOB_TYPE= (
    ('FullTime','FullTime'),
    ('PartTime','PartTime'),
    ('Remote','Remote'),
    ('Freelance','Freelance'),
)

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    company = models.ForeignKey('Company' , on_delete= models.SET_NULL,null=True,blank=True , related_name='job_company')
    created_at = models.DateTimeField(default=timezone.now)
    salary_start = models.IntegerField()
    salary_end = models.IntegerField()
    description = models.TextField(max_length=20000)
    vacancy = models.IntegerField()
    job_type = models.CharField(choices=JOB_TYPE , max_length=10)
    experience = models.IntegerField()
    category = models.ForeignKey('Category' , on_delete=models.CASCADE , related_name= 'job_category')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30)
    logo= models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=100)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name