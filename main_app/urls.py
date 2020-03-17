from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'), 
   path('about/', views.about, name='about'),
   path('rocks/', views.rocks_index, name='index'),
   path('rocks/<int:rock_id>/', views.rocks_detail, name='detail'),
]