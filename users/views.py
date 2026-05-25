from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        username   = request.POST['username']
        email      = request.POST['email']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
        role       = request.POST.get('role', 'tourist')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'users/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'users/register.html')

        user = CustomUser.objects.create_user(
            username=username, email=email,
            password=password1, role=role
        )
        login(request, user)
        messages.success(request, f'Welcome, {user.username}!')
        return redirect('trek-list')

    return render(request, 'users/register.html')

@login_required
def profile(request):
    bookings = request.user.bookings.all().order_by('-created_at')
    return render(request, 'users/profile.html', {'bookings': bookings})