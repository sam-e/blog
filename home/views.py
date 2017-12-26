# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

# Create your views here.
def base(request):
    return render(request, 'home/home_page.html')

def about(request):
	return render(request, 'home/about_page.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('register')

    else:
        form = CustomUserCreationForm()

    return render(request, 'home/register_page.html', {'form': form})
