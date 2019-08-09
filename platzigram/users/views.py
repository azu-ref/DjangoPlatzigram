"""users views"""
#django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#models
from django.contrib.auth.models import User
from users.models import Profile

#exceptions
from django.db.utils import IntegrityError

def login_view(request):
    """login views"""
    if request.method == 'POST':       
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
       
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            new_user = User.objects.create_user(username=username, password=passwd)

        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.email = request.POST['email']
        new_user.save()

        profile = Profile(user=new_user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')