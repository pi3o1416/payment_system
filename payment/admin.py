
from django.contrib import admin
from .models import Transection

# Register your models here.

@admin.register(Transection)
class TransectionAdmin(admin.ModelAdmin):
    list_display = ['tran_id', 'store_id', 'signature_key']
