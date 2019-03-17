from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('x_was_generated', views.generate_x, name='gen-x'),
]
