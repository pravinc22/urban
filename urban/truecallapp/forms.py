from django import forms
from truecallapp.models import true_form,careerModel

class true_sign(forms.ModelForm):
    class Meta():
        model =true_form
        fields =('__all__')

class job_form(forms.ModelForm):
    class Meta():
        model =careerModel
        fields=('__all__')
