from math import cos
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def generate_x(request):
    x = [i * 0.3 for i in range(11)]
    y = [3 * cos(i) ** 2 - i ** 0.5 for i in x]
    return render(request, 'index.html', {'x': x, 'y': y})