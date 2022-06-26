from django.shortcuts import render
from django.http import HttpResponse
from random import shuffle


def generate_numbers(n):
    data = list(range(1, 10))
    shuffle(data)
    res = data[:n]
    print(res)
    return res


secret = generate_numbers(4)
actual = []


def sum_calc(request):
    if request.method == "GET":
        return render(request, 'create.html')
    elif request.method == 'POST':
        number_1 = request.POST.get('number')
        list1 = list(number_1.split())
        list2 = list(map(int, list1))
        global actual
        actual = list2

