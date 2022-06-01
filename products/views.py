from django.shortcuts import render
from products.models import Products

# Create your views here.
def products(request):
    producto = Products.objects.all()
    context = {'producto':producto}
    return render(request,'products.html', context = context)