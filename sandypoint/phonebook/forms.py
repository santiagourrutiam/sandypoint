from django import forms

from django.forms import ModelForm
from phonebook.models import UserProfileInfo, Sitrep, Contact
from django.contrib.auth.models import User

class AddSitrepForm (forms.ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta():
        model = Sitrep
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('department',)
    


CONTACT_TYPE_CHOICES = [
                ('Airport', 'AIRPORT'),
                ('CUSTOMS','Customs'),
                ('SHIPPING','Shipping'),
                ('TRANSPORT','Transport'),
                ('PROVIDERS','Providers'),
                ('ACCOMODATION','Hotels/Accomodation'),
                ('ALE','ALE Staff'),
            ]

class AddNewContactForm(forms.ModelForm):
    description = forms.CharField(
        max_length=400, 
        required=False, 
        widget=forms.Textarea(
            attrs={'class':'form-control'
            }
        )
    )
    class Meta():
        model = Contact
        fields = '__all__' 

# class SearchForm(forms.Form):
#     query = forms.CharField(label=_('Query'), max_length=100,
#                             widget=forms.TextInput(attrs={'class': 'form-control system-search', 'required': '',
#                                                           'tabindex': 1, 'autofocus': '1',
#                                                           'placeholder': _('Search contact')}))
