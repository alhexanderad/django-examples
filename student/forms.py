from django import forms
from .models import Assistance

class AssistanceForm(forms.ModelForm):
  class Meta:
    model =Assistance
    fields = "__all__"