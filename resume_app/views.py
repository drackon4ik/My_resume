from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import CustomerForm, NewUserForm
from .models import Customer


def home(request):
    return render(request, 'toform.html')


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            user_info = {'username': username, 'password': password}
            return login_request(request, user_info)
        else:
            return render(request=request, template_name="register.html", context={"register_form": form})
        # messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def resume(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()

            first_name = form.cleaned_data.get('first_name')
            second_name = form.cleaned_data.get('second_name')
            skills = form.cleaned_data.get('skills')
            education = form.cleaned_data.get('education')
            email = form.cleaned_data.get('email')
            return render(request, 'template1.html', context={'first_name': first_name, 'second_name': second_name,
                                                              'skills': skills, 'education': education,
                                                              'email': email})
    else:
        form = CustomerForm
        return render(request, 'index.html', context={'form': form})


def login_request(request, user_info=None):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/resume_app/")
            else:
                messages.error(request, "Invalid username or password.")
                print(messages.error(request, "Invalid username or password."))
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    if user_info:
        form.fields['username'].initial = user_info.get('username')
        form.fields['password'].initial = user_info.get('password')
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/resume_app/")
