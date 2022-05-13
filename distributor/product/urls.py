from djano.urls import path
from . import views

app_name='product'

urlpatterns = [
    path('',views.product_index,name='product_index'),
]
