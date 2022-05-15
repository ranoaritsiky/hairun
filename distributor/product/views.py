from multiprocessing import context
from django.shortcuts import render
from .models import Product
from .forms import Product_forms

# Create your views here.

# def product_form(request):
def product_index(request):
    # TODO:retrieve all data in product
    latest_product=Product.objects.order_by('-create_date')

    form=Product_forms()
    if request.method == 'POST':
        form=Product_forms(request.POST)
        if form.is_valid():
            print('valid ve')
            form.save()
        else:
            print('NOT VALID')
    
    context = {
        'form':form,
        'latest_product':latest_product,
        }
    # product=product.objects.order_by('-create_date')[:8]
    # context={
    #     'product':product,
    # }
    return render(request,'product_templates/index.html',context)


# def product_list(request):
#     latest_product=Product.objects.order_by('-create_date')
#     context={
#         'latest_product':latest_product,
#     }
#     return render (request,'product/product_list.html',context)
