from django import forms
from django.core.validators import FileExtensionValidator
from .models import JobApply

class JobApplyForm(forms.ModelForm):
    cv = forms.FileField(
        label ='CVS',
        widget = forms.ClearableFileInput(attrs={'accept': '.pdf'}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf'] , message='Only PDF files are allowed')]
    )
    class Meta :
        model = JobApply
        fields = ['username','email','linkedin_profile','github_profile','cv','cover_letter']