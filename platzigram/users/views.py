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

#forms
from users.forms import ProfileForm

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

@login_required
def update_profile(request):
    """Update a user's profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()
            
            return redirect('update_profile')
    else:        
        form = ProfileForm()

    return render(
        request, 
        'users/update_profile.html', 
        {
            'profile': profile,
            'user': request.user,
            'form': form,      
        }
    )