from django.urls import path
from . import views

app_name='product_app'

urlpatterns = [
    path('',views.product_index,name='product_index'),

    path('delete/', views.product_delete, name='product_delete'),
    # path('product_list/',views.product_list,name='product_list'),
]
