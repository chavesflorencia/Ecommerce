from django.shortcuts import render
from products.models import Products

# Create your views here.
def products(request):
    producto_nuevo = Products.objects.create(
        name = 'Agua',
        description = 'la mas rica',
        SKU= 'JSH987HY'
    )
    context = {'producto_nuevo':producto_nuevo}
    return render(request,'products.html', context = context)