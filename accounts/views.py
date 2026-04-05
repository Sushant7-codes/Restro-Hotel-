from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
# Create your views here.


def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return render(request, 'accounts/login.html')
    else:
        form=CustomUserCreationForm()
        
    return render(request, 'accounts/register.html', {'form':form})

def login(request):
    return render(request, 'accounts/login.html')