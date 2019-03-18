from functools import reduce
from math import cos
from operator import mul
from django.shortcuts import HttpResponse, render


def my_variant(x):
    return 3 * cos(x) ** 2 - x ** 0.5


def gen_xy():
    x = [i * 0.3 for i in range(11)]
    y = [my_variant(i) for i in x]
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


def x_and_y_to_csv(x, y):
    return None if len(x) != len(y) else 'xp,yp\n' + '\n'.join([str(x[i]) + ',' + str(y[i]) for i in range(len(x))])


def index(request, stage=0):
    context = {}
    if stage > 0:
        x, y = gen_xy()
        context['x'], context['y'] = x, y
    if stage > 1:
        context['y_gen_by_i'] = [interpolation(i) for i in x]
        context['polynomial'] = str_interpolation()
    return render(request, 'index.html', context=context)


def data(request):
    x = [i * 0.03 for i in range(101)]
    y = [my_variant(i) for i in x]
    return HttpResponse(x_and_y_to_csv(x, y), content_type='text/csv')


def data_interpolated(request):
    x = [i * 0.03 for i in range(101)]
    y_interpolate = [interpolation(i) for i in x]
    return HttpResponse(x_and_y_to_csv(x, y_interpolate), content_type='text/csv')


def data_bial(request):
    x = [i * 0.03 for i in range(101)]
    y_bial = [(interpolation(i) - my_variant(i)) for i in x]
    return HttpResponse(x_and_y_to_csv(x, y_bial), content_type='text/csv')