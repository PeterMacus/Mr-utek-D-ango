from django.shortcuts import render, HttpResponse
from . import views

def index(request):
        if request.method == "GET":
                vysledok = 0
        if request.method == "POST":
                try:
                        a = int(request.POST['a'])
                        b = int(request.POST['b'])
                except:
                        vysledok = ""
                operator = request.POST['operator']
                try:
                        if operator == "+":
                                vysledok = a+b
                        elif operator == "-":
                                vysledok = a-b
                        elif operator == "*":
                                vysledok = a*b
                        elif operator == "/":
                                try:
                                        vysledok = a/b
                                except:
                                        vysledok="Nemozete delit nulou"
                except:
                        vysledok = "musite zadat cislo"
        return render(request, 'cisla/index.html', dict(vysledok=vysledok))