from django.forms import ModelForm
from main.models import Product

class NewProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "image", "description", "price", "stock"]