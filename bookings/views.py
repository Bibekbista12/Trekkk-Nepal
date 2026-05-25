from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from treks.models import Trek
from .models import Booking

@login_required
def create_booking(request, slug):
    trek = get_object_or_404(Trek, slug=slug)
    if request.method == 'POST':
        trek_date  = request.POST.get('trek_date')
        num_people = int(request.POST.get('num_people', 1))
        special    = request.POST.get('special_req', '')

        booking = Booking.objects.create(
            user       = request.user,
            trek       = trek,
            trek_date  = trek_date,
            num_people = num_people,
            special_req = special,
        )
        messages.success(request, f'Booking confirmed! Total: ${booking.total_price}')
        return redirect('my-bookings')

    return redirect('trek-detail', slug=slug)

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})

@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if booking.status == 'pending':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, 'Booking cancelled.')
    return redirect('my-bookings')