from django import forms

from pagedown.widgets import PagedownWidget

from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "payment_form",
            "status",
            "details",
        ]