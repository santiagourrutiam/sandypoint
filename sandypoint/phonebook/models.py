from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Additional
    department = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    CHOICES = [
                ('AIRPORT','Airport'),
                ('CUSTOMS','Customs'),
                ('SHIPPING','Shipping'),
                ('TRANSPORT','Transport'),
                ('PROVIDERS','Providers'),
                ('ACCOMODATION','Hotels/Accomodation'),
                ('ALE','ALE Staff')
            ]

    firstname       = models.CharField(verbose_name="Firstname", max_length=100)
    lastname        = models.CharField(verbose_name="Lastname", max_length=100, null=True)
    company         = models.CharField(verbose_name="Company", max_length=100,default='Company')
    contact_type    = models.CharField (choices=CHOICES,max_length=100, default='Providers')
    phone           = models.CharField(verbose_name="Phone", max_length=100)
    mobile_phone    = models.CharField(verbose_name="Mobile phone", max_length=100, blank=True)
    email           = models.EmailField(verbose_name="Email", max_length=100, null=True)
    description     = models.CharField(verbose_name="Descripcion", max_length=200, null=True, default='No description provided')

    def __unicode__(self):
        return u"%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
