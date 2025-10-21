from django.shortcuts import render, HttpResponse
from . import views

def index(request):
        if request.method == "GET":
                vacsie = ""
                parneA = ""
                parneB = ""
                prvoA = ""
                prvoB = ""
        if request.method == "POST":
            try:
                a = int(request.POST['a'])
                b = int(request.POST['b'])
            except:
                a = ""
                b = ""
        try:
                if a>b:
                    vacsie = "Cislo a je vacsie ako cislo b"
                elif b>a:
                    vacsie = "Cislo b je vacsie ako cislo a"
                elif a==b:
                    vacsie = "Cisla su rovne"
                else:
                    vacsie = "Error"
                
                parneA = parne(a)
                parneB = parne(b)

                prvoA = prvocislo(a)
                prvoB = prvocislo(b)
        except:
                vacsie = "Zadaj cislo"
                parneA = ""
                parneB = ""
                prvoA = ""
                prvoB = ""
        return render(request, 'kalkulacka/index.html', {"vacsie":vacsie, "parneA": parneA, "parneB": parneB, "prvoA": prvoA, "prvoB": prvoB})

def parne(cislo):
      if cislo % 2 == 0:
            return "Parne"
      else:
            return "Neparne"
      
def prvocislo(cislo):
      if cislo == 1:
           return "Nie je prvocislo"

      for i in range(2, cislo):
        if cislo%i == 0:
             return "Nie je prvocislo"
      return "Je prvocislo"