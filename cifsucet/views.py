from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == 'GET':
        number = ""
        output = ""
        return render(request, "cifsucet/index.html", {'output':output,'number':number})
    if request.method == 'POST':
        number = str(request.POST['number'])
        field = [int(d) for d in str(number) ]
        output = sum(field)
    output = f"Ciferny sucet je{output}"
    return render(request, "cifsucet/index.html", {'output':output,'number':number})
