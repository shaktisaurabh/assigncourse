from assigncourseapp.models import course
from django import forms
class courseform(forms.ModelForm):
    class Meta:
        model = course
        fields = '__all__'