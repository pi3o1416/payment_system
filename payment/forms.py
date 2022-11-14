
from django import forms
from .models import Transection

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Transection
        fields = ['transection_amount', 'customer_name', 'customer_email', 'customer_address', 'customer_phone_no']


