
from django.shortcuts import render, redirect
from django.views import View
from .forms import PaymentForm

# Create your views here.

def payment_success(request):
    return render(request, template_name='payment/success.html')

def payment_failed(request):
    return render(request, template_name='payment/failed.html')

def payment_canceled(request):
    return render(request, template_name='payment/cancel.html')

def make_payment(request):
    form = PaymentForm()
    return render(request, template_name='payment/make_payment.html', context={'payment_form': form})

class MakePayment(View):
    form = PaymentForm

    def get(self, request):
        return render(request, template_name='payment/make_payment.html', context={'payment_form': self.form()})

    def post(self, request):
        form = self.form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='payment:make-payment')
        return render(request, template_name='payment/make_payment.html', context={'payment_form': form})


