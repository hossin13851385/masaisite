from django.shortcuts import render

# Create your views here.
def category(request):
    return render (request , 'product/list-category.html')


def single(request):
    return render (request , 'product/single-product.html')