from django import forms
from django.core.validators import FileExtensionValidator
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import JobApply , Job

class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label ='CVS',
        widget = forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'] , message='Only PDF files are allowed')]
    )
    class Meta :
        model = JobApply
        fields = ['username','email','linkedin_profile','github_profile','cv','cover_letter']



class JobForm(forms.ModelForm):
    description = forms.CharField(widget=SummernoteWidget())

    class Meta :
        model = Job
        fields = ['title','location','company','salary_start','salary_end','description','vacancy','job_type','experience','category']
