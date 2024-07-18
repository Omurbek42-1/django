from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.text_response_view, name='text-response'),
    path('objects/', views.object_response_view, name='object-response'),
    path('html/', views.html_template_view, name='html-response'),
]
