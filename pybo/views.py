from django.shortcuts import render, redirect

def pybo(request):
    return render(request, 'pybo/pybo.html')