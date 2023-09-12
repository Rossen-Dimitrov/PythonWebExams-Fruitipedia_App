from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('Fruitipedia_App.profile_app.urls')),
    path('', include('Fruitipedia_App.fruit_app.urls')),

]

