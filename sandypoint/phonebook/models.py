from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)

    #Additional field Department
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
    primary_phone   = models.CharField(verbose_name="Phone", max_length=100)
    mobile_phone    = models.CharField(verbose_name="Mobile phone", max_length=100, blank=True)
    email           = models.EmailField(verbose_name="Email", max_length=100, null=True)
    description     = models.CharField(verbose_name="Descripcion", max_length=500, null=True, default='No description provided')
    date_added      = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __unicode__(self):
        return u"%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


class Sitrep(models.Model):
    name        = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    sitrep_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Sitrep'
        verbose_name_plural = 'Sitreps'
    
    def __unicode__(self):
        return u"Sitrep de: %s" % (self.name) 

    def __str__(self):
        return u"Sitrep de: %s %s" % (self.name,self.sitrep_time)