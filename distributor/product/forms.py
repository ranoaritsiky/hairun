from django import forms
from django.forms import ModelForm

from .models import Product

class Product_forms(ModelForm):
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    class Meta:
        model=Product
        fields='__all__'