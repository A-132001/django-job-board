from django import forms
from .models import Applyers,Job
class Applyers_form(forms.ModelForm):
    class Meta:
        model = Applyers
        fields = ["name",'email','Profile_link','cv','coverletter']


class Job_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
        exclude = ('owner','slug')

