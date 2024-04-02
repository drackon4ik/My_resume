from django.forms import ModelForm
from .models import Customer

# creating a form


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
