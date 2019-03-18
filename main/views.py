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


def str_interpolation():
    x, y = gen_xy()
    return 'Nn(x) = ' + '+'.join([
        'f(' + ';'.join(['{:.1f}'.format(x[j]) for j in range(i + 1)]) + ')' +
        ''.join(['(x-{:.1f})'.format(x[j]) for j in range(i)])
        for i in range(len(x))
    ])


def index(request, stage=0):
    context = {}
    if stage > 0:
        x, y = gen_xy()
        context['x'], context['y'] = x, y
    if stage > 1:
        context['y_gen_by_i'] = [interpolation(i) for i in x]
        context['polynomial'] = str_interpolation()
    return render(request, 'index.html', context=context)
