# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

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
      form = UserChangeForm(request.POST, instance=request.user)
      if form.is_valid():
         form.save()

         return redirect('accounts/editprofile_page.html')

      else:
         form = UserChangeForm(instance=request.user)
         return render(request, 'accounts/editprofile_page.html', {'form': form})
