from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:stage>', views.index, name='main-page'),
]
