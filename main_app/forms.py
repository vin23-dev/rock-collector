from django.forms import ModelForm
from .models import Quality

class QualityForm(ModelForm):
  class Meta:
    model = Quality
    fields = ['date', 'quality']