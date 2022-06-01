from multiprocessing import context
from django.shortcuts import render

def probando (request):
    context= {
        'nombre': 'Florchaaaa'   
    }
    return render(request,'template.html',context = context)
def index (request):
    return render (request, 'index.html')