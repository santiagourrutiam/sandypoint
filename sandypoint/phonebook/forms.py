"""
@Santiago Urrutia
phonebook/forms.py

Contains all forms of the application.
1) AddSitrepForm class (name, description)
2) UserForm
3) UserProfileInfoForm

"""

from django import forms
from django.forms import ModelForm
from phonebook.models import UserProfileInfo, Sitrep, Contact
from django.contrib.auth.models import User

#1)
class AddSitrepForm (forms.ModelForm):
    name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta():
        model = Sitrep
        fields = '__all__'

#2)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

#3)
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('department',)
    
class AddNewContactForm(forms.ModelForm):
    description = forms.CharField(
        max_length=400, 
        required=False, 
        widget=forms.Textarea(
            attrs={'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        max_length=200,
        required=False)
    
    class Meta():
        model = Contact
        fields = '__all__' 