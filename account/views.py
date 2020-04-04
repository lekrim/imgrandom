from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from account.models import Profile
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Profile.objects.create(user=new_user)
            messages.success(request, 'registration completed successfully', fail_silently=True)
            return redirect('account:login')
        else:
            form = UserRegistrationForm(request.POST)
            messages.error(request, 
                           'check your password, may be it is too common or password1 doesnt match password2', 
                           fail_silently=True)
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form':form})

@login_required
def edit_account(request):
    if request.method == "POST":
        form = UserRegistrationForm(instance=request.user, data=request.POST)
        if form.is_valid():
            user_edit = form.save(commit=False)
            user_edit.set_password(form.cleaned_data['password1'])
            user_edit.save()
            messages.success(request, 'Account updated successfully', fail_silently=True)
            return redirect('account:login')
        else:
            messages.error(request, 
                           'check your username or password, may be it is too common or password1 doesnt match password2', 
                           fail_silently=True)
    else:
        form = UserRegistrationForm()
    return render(request, 'account/edit.html', {'form':form})

