from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ['user', 'trek', 'trek_date', 'num_people', 'total_price', 'status']
    list_filter   = ['status', 'trek_date']
    search_fields = ['user__email', 'trek__name']
    list_editable = ['status']