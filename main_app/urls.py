from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'), 
   path('about/', views.about, name='about'),
   path('rocks/', views.rocks_index, name='index'),
   path('rocks/<int:rock_id>/', views.rocks_detail, name='detail'),
   path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
   path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
   path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'), 
   path('rocks/<int:rock_id>/add_quality/', views.add_quality, name='add_quality'),
   path('rocks/<int:rock_id>/assoc_region/<int:region_id>/', views.assoc_region, name='assoc_region'),
   path('rocks/<int:rock_id>/unassoc_region/<int:region_id>/', views.unassoc_region, name='unassoc_region'),
   path('regions/', views.RegionList.as_view(), name='regions_index'),
   path('regions/<int:pk>/', views.RegionDetail.as_view(), name='regions_detail'),
   path('regions/create/', views.RegionCreate.as_view(), name='regions_create'),
   path('regions/<int:pk>/update/', views.RegionUpdate.as_view(), name='regions_update'),
   path('regions/<int:pk>/delete/', views.RegionDelete.as_view(), name='regions_delete'),
   path('accounts/signup/', views.signup, name='signup'), 
]