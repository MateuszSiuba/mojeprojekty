from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse("Witaj w Django!")

def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

def show_time(request):
    now = datetime.now()
    
    current_date = now.strftime("%d.%m.%Y")
    current_time = now.strftime("%H:%M")
    
    context = {
        "date": current_date,
        "time": current_time
    }
    
    return render(request, "witaj/time.html", context)