from django.shortcuts import render, HttpResponse
from . import views

def index(request):
    if request.method == "GET":
        vysledok = 0
    if request.method == "POST":
        
    try:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
                a = float(input("Zadaj prvé číslo: "))
                b = float(input("Zadaj druhé číslo: "))
            except ValueError:
                print("Zadaná hodnota nie je číslo")
            vysledok = a / b
       




    return render(request, 'kalkulacka/index.html',dict(vysledok=vysledok))


