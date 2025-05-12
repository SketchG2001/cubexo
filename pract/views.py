from django.shortcuts import render, redirect
from .models import Adult, Person
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'register.html', {'form': form})


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            return render(request, 'profile.html', {'u_form': u_form, 'p_form': p_form})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'profile.html', context)


def home_page(request):
    persons = Person.objects.all()
    adults = Adult.objects.filter(age__gte=18)
    context = {'adults': adults}
    return render(request, 'homepage.html', context)
