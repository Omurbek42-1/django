from django.urls import path
from .views import create_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    # другие пути
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')),  # Замените 'your_app_name' на имя вашего приложения
]

