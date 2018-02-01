# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages

from .forms import RegistrationForm, ProfileForm

# Create your views here.
def register(request):
   if request.method == 'POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('base')

   else:
      form = RegistrationForm()
      return render(request, 'accounts/register_page.html', {'form': form})

def view_profile(request):
   args = { 'user': request.user }
   return render(request, 'accounts/profile_page.html', args)

def edit_profile(request):
   if request.method == 'POST':
      profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
      if profile_form.is_valid():
         profile_form.save()
         messages.success(request, ('Your profile was successfully updated!'))
         return redirect('edit_profile')
      else:
         messages.error(request, ('Please correct the error below.'))
   else:
      profile_form = ProfileForm(instance=request.user.userprofile)
   return render(request, 'accounts/editprofile_page.html', {
      'profile_form': profile_form
   })
