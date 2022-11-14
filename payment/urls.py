
from django.urls import path
from .views import payment_canceled, payment_failed, payment_success, MakePayment

app_name='payment'
urlpatterns = [
    path('', MakePayment.as_view(), name='make-payment'),
    path('success/', payment_success, name='payment-success'),
    path('failed/', payment_failed, name='payment-failed'),
    path('canceled/', payment_canceled, name='payment-canceled'),
]
