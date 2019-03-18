from functools import reduce
from math import cos
from operator import mul
from django.shortcuts import render


def gen_xy():
    x = [i * 0.3 for i in range(11)]
    y = [3 * cos(i) ** 2 - i ** 0.5 for i in x]
    return x, y


def f(xs, ys):
    if len(xs) == 1:
        return ys[0]
    else:
        return (f(xs[1:], ys[1:]) - f(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])


def interpolation(x):
    x_array, y_array = gen_xy()
    return sum(
        [f(x_array[:i + 1], y_array[:i + 1]) * 
        reduce(mul, [x - x_array[j] for j in range(i)], 1) 
        for i in range(len(x_array))]
    )


def index(request):
    return render(request, 'index.html')


def generate_x(request):
    x, y = gen_xy()
    return render(request, 'index.html', {'x': x, 'y': y})

def calc_y_by_interpolation(request):
    x, y = gen_xy()
    test = [interpolation(i) for i in x]
    return render(request, 'index.html', {'x': x, 'y': y, 'test': test})