from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calculate(request):
    month = int(request.GET.get('month', 1))
    salary = int(request.GET.get('salary', 10000))
    amount = salary * month
    return HttpResponse(f'Ваша заработная плата за {month} месяцев составляет {amount}')