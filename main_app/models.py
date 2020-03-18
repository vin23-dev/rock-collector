from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

QUALITY = (
    ('R', 'Rough'),
    ('F', 'Fair'),
    ('P', 'Pristine')
)

RARITY = (
    ('C', 'Common'),
    ('U', 'Uncommon'),
    ('R', 'Rare'),
    ('E', 'Epic'),
    ('L', 'Legendary')
)

class Region(models.Model):
  name = models.CharField(max_length=50)
  rarity = models.CharField(
    max_length=1,
    choices=RARITY,
    default=RARITY[0][0]
  )
  

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('regions_detail', kwargs={'pk': self.id})

class Rock(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  regions = models.ManyToManyField(Region)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'rock_id': self.id})  

class Quality(models.Model):
  date = models.DateField('date found')
  quality = models.CharField(
    max_length=1,
    choices=QUALITY,
    default=QUALITY[0][0]
  )
  rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_quality_display()} on {self.date}"

  class Meta:
    ordering = ['-date']  



  