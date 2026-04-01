from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def aralin(request):
    return render(request, 'aralin.html')

def talahayanan(request):
    return render(request, 'talahayanan.html')