from django import forms
from django import forms
from en.models import User
class StudentForm(forms.ModelForm):
    class Meta:
        Model=User
        forms=['name','roll','address']