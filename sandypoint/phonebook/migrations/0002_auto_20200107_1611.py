# Generated by Django 2.2.5 on 2020-01-07 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(default='Company', max_length=100, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.CharField(default='Description', max_length=200, null=True, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='lastname',
            field=models.CharField(max_length=100, null=True, verbose_name='Lastname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile_phone',
            field=models.CharField(max_length=100, null=True, verbose_name='Mobile phone'),
        ),
    ]
