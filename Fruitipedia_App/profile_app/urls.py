
from django.urls import path, include

from Fruitipedia_App.profile_app import views


urlpatterns = [
    path('create/', views.profile_create, name='profile_create_page'),
    path('edit/', views.profile_edit, name='profile_edit_page'),
    path('delete/', views.profile_delete, name='profile_edit_page'),
    path('details/', views.profile_details, name='profile_details_page'),

]
