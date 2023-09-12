from django.urls import path, include

from Fruitipedia_App.fruit_app import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('dashboard/', views.dashboard, name='dashboard_page'),
    path('create/', views.create_fruit, name='create_fruit_page'),
    path('<fruitId>/', include([
        path('details/', views.details_fruit, name='details_fruit_page'),
        path('edit/', views.edit_fruit, name='edit_fruit_page'),
        path('delete/', views.delete_fruit, name='delete_fruit_page'),
    ])),
]
