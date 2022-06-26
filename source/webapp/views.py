from django.shortcuts import render



def sum_calc(request):
    if request.method == "GET":
        return render(request, 'create.html')
    elif request.method == 'POST':
        number_1 = request.POST.get('number')
        list1 = list(number_1.split())
        list2 = list(map(int, list1))
        actual = list2

