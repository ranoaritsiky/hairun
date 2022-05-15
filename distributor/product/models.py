from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=50,)
    create_date = models.DateTimeField(auto_now_add=True,)
    
    def __str__(self):
        return self.name