# phonebook/views.py
"""
@Santiago Urrutia
Contains all Views.
"""
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from phonebook.models import Contact, UserProfileInfo, Sitrep
from phonebook.forms import AddNewContactForm, UserForm, UserProfileInfoForm, AddSitrepForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import ContactFilter
from django.db.models import Q
from django.views.generic import ListView
from django.utils.timezone import datetime 
#-------------------------------------------------------------------------
@login_required
def SearchResultsView (request):
    query = request.GET.get('q')
    object_list = Contact.objects.filter(
                                        Q(firstname__icontains=query) | 
                                        Q(lastname__icontains=query) |
                                        Q(contact_type__icontains=query) |
                                        Q(company__icontains=query)
                                        )
    context = {'object_list':object_list}
    return render(request, 'phonebook/search_results.html', context)
#-------------------------------------------------------------------------
#THE MAIN 
@login_required
def showAllContacts(request):
    queryset = Contact.objects.all()
    context = {
        'object_list': queryset,
    }
    return render (request, 'phonebook/front_page.html',context)

#-------------------------------------------------------------------------
#SITREP SECTION [ADD SITREP VIEW | SHOW SITREPS VIEW]
@login_required
def addNewSitrep(request):
    form = AddSitrepForm()
    if request.method == 'POST':
        form = AddSitrepForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return showAllSitrep(request)
        else:
            print ('Error, Form Invalid')
    return render (request, 'phonebook/add_sitrep.html', {'form':form})

#-------------------------------------------------------------------------
@login_required
def showAllSitrep (request):
    today = datetime.today()
    queryset = Sitrep.objects.filter(sitrep_time__year=today.year, sitrep_time__month=today.month, sitrep_time__day=today.day).order_by('sitrep_time')
    return render (request, 'phonebook/show_sitrep.html',{'object_list': queryset})
#-------------------------------------------------------------------------
@login_required
def user_logout (request):
    logout(request)
    return HttpResponseRedirect(reverse('phonebook:userLogin'))
#-------------------------------------------------------------------------
#REGISTRATION PAGE FOR NEW USERS
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
#-------------------------------------------------------------------------
#ADD NEW CONTACT VIEW
@login_required
def addContact(request):
    form = AddNewContactForm()
    if request.method == 'POST':
        form = AddNewContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return showAllContacts(request)
        else:
            print ('Error, Form Invalid')

    return render (request, 'phonebook/add_contact.html', {'form':form})
#-------------------------------------------------------------------------
#FILTERED BY CONTACT TYPE SEARCH
@login_required
def filteredContacts (request):
    contact_list = Contact.objects.all()
    contact_filter = ContactFilter(request.GET, queryset=contact_list)
    
    return render(request, 'phonebook/filtered_search.html', {'filter': contact_filter})
    
#-------------------------------------------------------------------------
def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get ('username')
        password = request.POST.get ('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('phonebook:showAllContacts'))
            else:
                return HttpResponse ('Account not active')
        else:
            print ('Someone tried to login and failed!')
            print ('Username: {} and Password: {}'.format(username,password))
            return HttpResponse('invalid login details')
    else:
        return render (request, 'phonebook/login.html',{})


