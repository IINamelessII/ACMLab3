from django.urls import path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('x_was_generated', views.generate_x, name='gen-x'),
    path('interpolation', views.calc_y_by_interpolation_and_str, name='interpolation'),
]
