from django.shortcuts import render

def inicio(request):
    return render(request,'../../falcao/templates/index.html')