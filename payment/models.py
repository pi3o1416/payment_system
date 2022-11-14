import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


def generate_transection_id():
    transection_id = uuid.uuid4().hex
    return transection_id


class Transection(models.Model):
    class TransectionStatus(models.IntegerChoices):
        INITIATED = 0, _("Payment Initiated")
        ATTEMPT = 1, _("Payment Attempt")
        SUCCESSFUL = 2, _("Payemnt Successful")
        CANCELED = 3, _("Payment Canceled")
        CHARGEBACK = 4, _("Payment Charge-back")
        ON_HOLD = 5, _("Payment on hold")
        SUSPECT_FRAUD = 6, _("Suspect fraud")
        FAILED = 7, _("Payment failed")
        REFUNDED_BANK = 8, _("Payment Refunded by bank")
        INCOMPLETE = 9, _("Payment Incomplete")
        REFUND_VOID = 10, _("Payment Refund")
        ERROR = 11, _("Payment Error")
        CHARGEBACK_REFUND = 12, _("Payment Refund due to Chargeback lost")
        MISSING_AUTHORIZED_EMAIL = 13, _("Customer Documents Missing")

    transection_id = models.CharField(
        _("Transaction Id"),
        max_length=32,
        default = generate_transection_id,
        editable=False,
        unique=True,
    )
    transection_amount = models.DecimalField(
        _("Transection amount"),
        max_digits=15,
        decimal_places=3
    )
    transection_status = models.IntegerField(
        _("Transection Status"),
        choices=TransectionStatus.choices,
        default=TransectionStatus.INITIATED
    )
    transection_time = models.DateTimeField(
        _("Transection Time"),
        auto_now_add=True
    )
    customer_name = models.CharField(
        _("Customer Fullname"),
        max_length = 100
    )
    customer_email = models.EmailField(
        _("Customer Email"),
    )
    customer_address = models.CharField(
        _("Customer Address"),
        max_length = 100,
        default="Dhaka"
    )
    customer_phone_no = models.CharField(
        _("Customer Phone no"),
        max_length = 14
    )


