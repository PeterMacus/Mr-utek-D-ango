from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == 'GET':
        cislo = ""
        output = ""
    if request.method == 'POST':
        try:
            cislo = int(request.POST['cislo'])
        except ValueError:
            return render(request, "prvocisla/index.html", { 'output': "Nedal si cislo"})
        if cislo <= 1:
            output = "Nie je prvocislo"
        else:
            output = "Je prvocislo"
            for i in range(2,cislo):
                if cislo%i == 0:
                    output = "Nie je prvocislo" 
                    break
        return render(request, "prvocisla/index.html", {'output':output, 'cislo':cislo})


    

    