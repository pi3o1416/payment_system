# Generated by Django 4.1.3 on 2022-11-13 09:20

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transection',
            name='tran_id',
            field=models.CharField(default=payment.models.generate_transection_id, editable=False, max_length=32, unique=True, verbose_name='Transaction Id'),
        ),
    ]
