from django import forms
from .models import Contact
from django.forms import ModelForm
from phonebook.models import UserProfileInfo
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('department',)
    



# class LoginForm(forms.Form):
#     username = forms.CharField(label=_("Username"), max_length=30,
#                                widget=forms.TextInput(attrs={
#                                    'class': 'form-control',
#                                    'placeholder': _('Username'),
#                                    'required': '',
#                                    'tabindex': 1,
#                                    'autofocus': '1'}))

#     password = forms.CharField(label=_("Password"), widget=forms.PasswordInput(attrs={'class': 'form-control',
#                                                                                       'placeholder': _('Password'),
#                                                                                       'required': '', 'tabindex': 2}))

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
    class Meta:
        model = Contact
        fields = '__all__' 
    #     firstname = forms.CharField(label="Firstname",
    #                             max_length=100,
    #                             widget=forms.TextInput(attrs={
    #                                 'class': 'form-control',
    #                                 'required': False,
                                    
    #                             }
    # )
    # )

    # lastname    = forms.CharField (label="Lastname", 
    #                             max_length=100,
    #                             widget=forms.TextInput(attrs={
    #                                 'class': 'form-control',
    #                                 'required': '', 
                                    
    #                                 }
    #                             )
    #                         )
    # company     = forms.CharField (label="Company",
    #                             max_length=100,
    #                             widget=forms.TextInput(attrs={
    #                                 'placeholder':'Company',
    #                                 'class':'form-control',
    #                             }))
    
    # contact_type = forms.MultipleChoiceField (label="Contact Type",
    #                             widget=forms.CheckboxSelectMultiple(attrs={
    #                                         'class':'form-control', 
    #                             }),
    #                             choices=CONTACT_TYPE_CHOICES,
    #                             )

    # phone = forms.CharField(label="Phone", 
    #                         max_length=100, 
    #                         required=False,
    #                         widget=forms.TextInput(attrs={
    #                             'class': 'form-control',
    #                             'list-style':'none',
                                
    #                             }
    #                         )
    #                     )
    
    # mobile_phone = forms.CharField(label="Mobile phone", 
    #                                 max_length=100, 
    #                                 required=False,
    #                                widget=forms.TextInput(attrs={
    #                                    'class': 'form-control', 
                                       
    #                                    }
    #                             )
    #                         )
    
    # email = forms.EmailField(label="Email", 
    #                         max_length=100,
    #                          widget=forms.EmailInput(attrs={
    #                              'class': 'form-control', 
    #                              'required': '', 
                                 
    #                              }
    #                         )
    #                     )
    
    # description = forms.CharField(label="Description",
    #                                 required=False,
    #                                 max_length=300,
    #                                 widget = forms.Textarea(attrs={
    #                                     'placeholder': 'Enter description for the contact',
    #                                     'class': 'form-control',
    #                                 })
                                    
    #                             )


# class SearchForm(forms.Form):
#     query = forms.CharField(label=_('Query'), max_length=100,
#                             widget=forms.TextInput(attrs={'class': 'form-control system-search', 'required': '',
#                                                           'tabindex': 1, 'autofocus': '1',
#                                                           'placeholder': _('Search contact')}))
