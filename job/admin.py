from django.contrib import admin

from .models import Category , Job , Company



class JobAdmin(admin.ModelAdmin):
    list_display = ['title','location','company','job_type','vacancy', 'category']
    search_fields = ['title','category','description']
    list_filter = ['created_at', 'vacancy', 'experience' ,'job_type']


admin.site.register(Job,JobAdmin)
admin.site.register(Company)
admin.site.register(Category)