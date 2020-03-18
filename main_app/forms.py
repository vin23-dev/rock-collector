from django.forms import ModelForm
from .models import Quality
from .models import Region

class QualityForm(ModelForm):
  class Meta:
    model = Quality
    fields = ['date', 'quality']

class RarityForm(ModelForm):
  class Meta:
    model = Region
    fields = ['rarity']