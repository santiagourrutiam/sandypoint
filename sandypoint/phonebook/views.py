from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from .models import Contact, UserProfileInfo
from phonebook.forms import AddNewContactForm, UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

#FrontPAge that shows the phonebook list
def frontPage(request):
    queryset = Contact.objects.all()
    context = {
        'object_list': queryset,
    }
    return render (request, 'phonebook/front_page.html',context)

@login_required
def user_logout (request):
    logout(request)
    return HttpResponseRedirect(reverse('phonebook:frontPage'))

#Registration Page for new Users
def registerNewUser(request):
    
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_info_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_info_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print (user_form.errors, user_profile_info_form.errors)
    else:
        user_form = UserForm()
        user_profile_info_form = UserProfileInfoForm()            

    return render (request,'phonebook/registration.html',
                    {'user_form': user_form,
                     'user_profile_info_form':user_profile_info_form,
                     'registered':registered})

#Vista para carga el formulario que agrega un nuevo contacto.

def addContact(request):
    form = AddNewContactForm()
    if request.method == 'POST':
        form = AddNewContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return frontPage(request)
        else:
            print ('Error, Form Invalid')

    return render (request, 'phonebook/add_contact.html', {'form':form})


def user_login (request):

    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('phonebook:frontPage'))
            else:
                return HttpResponse ('Account not active')
        else:
            print ('Someone tried to login and failed!')
            print ('Username: {} and Password: {}'.format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render (request, 'phonebook/login.html',{})