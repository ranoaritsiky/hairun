from django.urls import path
from . import views

app_name='product_app'

urlpatterns = [
    path('',views.product_index,name='product_index'),
    # path('product_list/',views.product_list,name='product_list'),
]
