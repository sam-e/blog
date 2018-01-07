# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('register')

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register_page.html', {'form': form})

def view_profile(request):
    args = { 'user': request.user }
    return render(request, 'accounts/profile_page.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        return redirect('view_profile')

    else:
        form = UserChangeForm(instance=request.user)
        args =  { 'form': form }
        return render(request, 'accounts/editprofile_page.html', args)
