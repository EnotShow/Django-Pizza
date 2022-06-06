from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.models import User


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            if request.POST.get('submit') == 'login':
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = authenticate(request, username=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    return redirect('login')
            elif request.POST.get('submit') == 'signup':
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                password = request.POST.get('password')
                data = User(first_name=first_name, last_name=last_name, email=email, phone=phone)
                data.set_password(password)
                data.save()
                return redirect('home')
        elif request.method == 'GET':
            return render(request, 'pizza/sign_up.html')
