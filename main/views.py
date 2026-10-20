from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def items(request):
    return render(request, 'items.html')

def report(request):
    return render(request, 'report.html')

def contact(request):
    return render(request, 'contact.html')
