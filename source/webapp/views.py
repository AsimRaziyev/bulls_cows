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
        return HttpResponse(check_1(request, actual))


def check_1(request, actual):
    try:
        result_actual = [int(x) for x in actual]
        if len(result_actual) < 4 or len(result_actual) > 4:
            result = "Enter a number in the amount of 4"
            context = {
                "Result": result,
            }
            return render(request, 'create.html', context)
        set_actual = set(result_actual)
        if len(result_actual) == len(set_actual):
            pass
        else:
            result = "Contain the same numbers!"
            context = {
                "Result": result,
            }
            return render(request, 'create.html', context)
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in result_actual:
            if i not in list:
                result = "Enter numbers in the range 1-9"
                context = {
                    "Result": result,
                }
                return render(request, 'create.html', context)
    except ValueError:
        result = "The value should be integers"
        context = {
            "Result": result,
        }
        return render(request, 'create.html', context)
    # print(secret)
    bulls = 0
    cows = 0
    for i in range(len(actual)):
        if actual[i] == secret[i]:
            bulls += 1
        elif actual[i] in secret:
            cows += 1
    if bulls == 4:
        result = f' Winner {bulls} bulls'
        context = {
            "Result": result,
        }
        return render(request, 'create.html', context)
    elif bulls or cows:
        result = f'bulls {bulls}, cows {cows}'
        context = {
            "Result": result,
        }
        return render(request, 'create.html', context)
    else:
        result = 'No identical numbers'
        context = {
            "Result": result,
        }
        return render(request, 'create.html', context)
