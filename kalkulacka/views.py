from django.shortcuts import render, HttpResponse
from . import views

def index(request):
    if request.method == "GET":
        vysledok = 0
    if request.method == "POST":
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        operator = request.POST["operator"]
        if operator == "+":
            vysledok = a + b
        elif operator == "-":
            vysledok = a - b 
        elif operator == "*":
            vysledok = a * b
        else:
            vysledok = a / b

    return render(request, 'kalkulacka/index.html',dict(vysledok=vysledok))


