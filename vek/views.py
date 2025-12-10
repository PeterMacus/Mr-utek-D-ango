from django.shortcuts import render, HttpResponse
def index (request):
    if request.method == 'GET':
        name =""
        output = "" 
        
        return render(request,"vek/index.html", {'output':output, 'name':name})
    if request.method == 'POST':
        name = request.POST['name']
        date =  request.POST['date']      

        months = ["januar", "februar", "marec", "april", "maj", "jun", "jul", "august", "september", "oktober", "november", "december"]  
        day = int(date[:2])
        month = int(date[2:4])
        year = int(date[4:])
        monthtext = months[month-1]
        output = f"Ahoj{name} tvoje narodenie je {day}.{monthtext}.{year}"
        return render(request, "vek/index.html", {'output':output, 'name':name})

