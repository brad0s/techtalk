from django.shortcuts import render
from django.http import Http404

from .models import Product

# Create your views here.
def product_create_view(request):
  return null

def products_list_view(request):
  try:
    queryset = Product.objects.all();
  except Product.DoesNotExist:
    raise Http404("No products were found")
  return render(request, "products/product_list.html", {'object_list': queryset})

def products_detail_view(request, id):
  try:
    obj = Product.objects.get(id=id)
    context = {
      "object": obj
    }
  except Product.DoesNotExist:
    raise Http404("Product was not found")
  return render(request, "products/product_detail.html", context)
