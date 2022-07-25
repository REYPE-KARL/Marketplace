from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponse
from accounts.models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404


def signup(request):
    if request.method == "POST":

        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirpassword = request.POST.get("cpassword")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        # vérifie si les valeurs sont vides
        if user_name == "" or email == "" or password == "" or \
                confirpassword == "" or first_name == "" or last_name == "":
            if user_name == "":
                messages.error(request, 'Enter your username.', extra_tags='user_name')
            if email == "":
                messages.error(request, 'Enter your email.', extra_tags='email')
            if password == "":
                messages.error(request, 'Enter your password.', extra_tags='password1')
            if confirpassword == "":
                messages.error(request, 'Enter your confirm password.', extra_tags='password2')
            if first_name == "":
                messages.error(request, 'Enter your first name.', extra_tags='first_name')
            if last_name == "":
                messages.error(request, 'Enter your last name.', extra_tags='last_name')
            return redirect('signup')

        # vérifie si les mots de passe corespondent
        if password != confirpassword:
            messages.error(request, 'Passwords must match.', extra_tags='confirm')
            return redirect('signup')

        user = CustomUser.objects.create_user(
            email=email, user_name=user_name, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        # vérifie si les valeurs sont vides
        if email == "" or password == "":
            if email == "":
                messages.error(request, 'Enter your username.', extra_tags='email')
            if password == "":
                messages.error(request, 'Enter your password.', extra_tags='password')
            return redirect('login')

        # Connecter l'utilisateur
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Authentication failed. Please try again.', extra_tags='login')
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def profile_user(request, slug):
    user = get_object_or_404(CustomUser, slug=slug)
    return render(request, 'accounts/profile.html', context={"user": user})
