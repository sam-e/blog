# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'home/base.html')