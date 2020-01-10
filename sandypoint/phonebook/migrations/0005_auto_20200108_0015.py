# Generated by Django 2.2.5 on 2020-01-08 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_auto_20200107_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('AIRPORT', 'Airport'), ('CUSTOMS', 'Customs'), ('SHIPPING', 'Shipping'), ('TRANSPORT', 'Transport'), ('PROVIDERS', 'Providers'), ('ACCOMODATION', 'Hotels/Accomodation')], default='Contact-Local', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=100, verbose_name='Mobile phone'),
        ),
    ]
