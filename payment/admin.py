
from django.contrib import admin
from .models import Transection

# Register your models here.


@admin.register(Transection)
class TransectionAdmin(admin.ModelAdmin):
    pass
    list_display = ['transection_id', 'transection_status', 'transection_time',
                    'transection_amount', 'customer_name', 'customer_email',
                    'customer_phone_no']

    list_filter = ['transection_time', 'transection_status']
    search_fields = ['transection_id', 'customer_name', 'customer_email', 'customer_phone_no']
