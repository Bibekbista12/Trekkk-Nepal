from django.urls import path
from . import views

urlpatterns = [
    path('create/<slug:slug>/', views.create_booking, name='create-booking'),
    path('my-bookings/', views.my_bookings, name='my-bookings'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel-booking'),
]