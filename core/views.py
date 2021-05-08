from django.shortcuts import render, redirect
from django.contrib.auth import login
from . import forms

# Create your views here.
def home(request):
    return render(request,'home.html')



def sign_up(request):
    form = forms.SignUpForm()
    print('request.method ',request.method)
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        print('print ',form.is_valid())
        if form.is_valid():
            email =form.cleaned_data.get('email').lower()
            user = form.save(commit=False)
            user.username = email
            print('Usuario', user)
            user.save()
            login(request,user,backend='django.contrib.auth.backend.ModelBackend')
            return redirect('/')

    return render(request,'sign_up.html',{'form':form})

