# Generated by Django 2.2.5 on 2020-01-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0008_contact_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitrep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=400)),
                ('sitrep_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(default='No description provided', max_length=500, null=True, verbose_name='Descripcion'),
        ),
    ]
