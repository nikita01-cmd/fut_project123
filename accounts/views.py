
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import loginus, Userregistrion

def home(request):
    return render(request, 'home.html')




def registration(request):
    if request.method == 'POST':
        form =Userregistrion(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = Userregistrion()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = loginus(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = loginus()
    return render(request, 'login.html', {'form': form})
