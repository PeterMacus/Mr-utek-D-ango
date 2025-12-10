from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == 'GET':
        number = ""
        output = ""
        return render(request, "faktorial/index.html",{'number':number, 'output':output})
    if request.method == 'POST':
        number =  int(request.POST['number'])
        output = 1
        for i in range(1, number+1):
            output = i*output
        output = f"Faktorial cisla {number} je {output}"
    return render(request, "faktorial/index.html",{'number':number, 'output':output})
