import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

import random
from faker import Faker
from job.models import Category , Company , Job


def create_category(n):
    fake = Faker()
    for x in range(n):
        Category.objects.create(
            name = fake.name()
        )
    print(f"{n} categories was created successfully")

def create_company(n):
    faker = Faker()
    images = ['job_list1.png','job_list2.png','job_list3.png','job_list4.png']
    for x in range(n):
        Company.objects.create(
            name =faker.company(),
            website =faker.url(),
            subtitle =faker.text(),
            email =faker.email(),
            logo = f"company/{images[random.randint(0,3)]}"
        )
    print(f"{n} Companies was created successfully")

def create_job(n):
    faker = Faker()
    job_type = ['FullTime','PartTime','Remote','Freelance']
    for x in range(n):
        Job.objects.create(
            title =faker.name(),
            description =faker.text(),
            company = Company.objects.all().order_by('?')[0],
            vacancy = random.randint(1,5),
            salary_start = random.randint(2000,2500),
            salary_end = random.randint(5000,10000),
            category = Category.objects.all().order_by('?')[0],
            experience = random.randint(1,5),
            job_type = job_type[random.randint(0,3)]     
        )
    print(f"{n} Jobs was created successfully")


#create_category(5)
#create_company(100)
create_job(1000)
