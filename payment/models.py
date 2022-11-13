from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Transection(models.Model):
    tran_id = models.UUIDField(
        _("Transaction Id"),
        unique=True,
    )
    store_id = models.CharField(
        _("Store Id"),
        max_length = 200,
        default = "aamarpaytest"
    )
    signature_key = models.CharField(
        _("Signature Key"),
        max_length = 200,
        default = "dbb74894e82415a2f7ff0ec3a97e4183"
    )
    pass
