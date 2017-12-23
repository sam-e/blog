# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def login_base(request):
    return render(request, 'home/home_page.html')

def about(request):
	return render(request, 'home/about_page.html')
