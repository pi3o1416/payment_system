
import requests
from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .forms import PaymentForm
from .services import generate_dict_for_payment
from .models import Transection

# Create your views here.

@csrf_exempt
def payment_success(request):
    if request.POST:
        transection_id = request.POST.get("mer_txnid")
        transection = Transection.objects.get(transection_id=transection_id)
        transection.transection_status = Transection.TransectionStatus.SUCCESSFUL
        transection.save()
    return render(request, template_name='payment/success.html')

@csrf_exempt
def payment_failed(request):
    if request.POST:
        transection_id = request.POST.get("mer_txnid")
        transection = Transection.objects.get(transection_id=transection_id)
        transection.transection_status = Transection.TransectionStatus.FAILED
        transection.save()
    return render(request, template_name='payment/failed.html')

@csrf_exempt
def payment_canceled(request):
    if request.POST:
        transection_id = request.POST.get("mer_txnid")
        transection = Transection.objects.get(transection_id=transection_id)
        transection.transection_status = Transection.TransectionStatus.CANCELED
        transection.save()
    return render(request, template_name='payment/cancel.html')


class MakePayment(View):
    form = PaymentForm

    def get(self, request):
        return render(request, template_name='payment/make_payment.html', context={'payment_form': self.form()})

    def post(self, request):
        form = self.form(data=request.POST)
        if form.is_valid():
            transection = form.save()
            payment_api_body = generate_dict_for_payment(transection)
            response = requests.post(url=settings.PAYMENT_URL, data=payment_api_body)
            if response.status_code == 200:
                track = response.json()
                return redirect(settings.PAYMENT_SUCCESS_REDIRECT_URL + track)
            return redirect(to='payment:make-payment')
        return render(request, template_name='payment/make_payment.html', context={'payment_form': form})


