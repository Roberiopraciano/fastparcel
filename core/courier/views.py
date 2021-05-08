
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView


@login_required()
def home(request):
    return render(request,'home.html')
