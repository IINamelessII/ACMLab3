from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:stage>', views.index, name='main-page'),
    path('data.csv', views.data, name='data'),
    path('data_interpolated.csv', views.data_interpolated, name='data-interpolated'),
]
