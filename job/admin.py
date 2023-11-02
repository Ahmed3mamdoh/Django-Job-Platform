from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Category , Job , Company



class JobAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    list_display = ['title','location','company','job_type','vacancy', 'category']
    search_fields = ['title','category','description']
    list_filter = ['created_at', 'vacancy', 'experience' ,'job_type']
    summernote_fields = '__all__'
    

admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Category)