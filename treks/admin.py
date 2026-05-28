from django.contrib import admin
from .models import Trek, TrekImage
import cloudinary.uploader


class TrekImageInline(admin.TabularInline):
    model  = TrekImage
    extra  = 3
    fields = ['image', 'caption', 'is_cover']


@admin.register(Trek)
class TrekAdmin(admin.ModelAdmin):
    list_display        = ['name', 'region', 'difficulty', 'price', 'duration', 'is_featured', 'is_active']
    list_filter         = ['region', 'difficulty', 'is_featured', 'is_active']
    search_fields       = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable       = ['is_featured', 'is_active']
    inlines             = [TrekImageInline]


@admin.register(TrekImage)
class TrekImageAdmin(admin.ModelAdmin):
    list_display = ['trek', 'caption', 'is_cover', 'uploaded_at']

    def save_model(self, request, obj, form, change):
        if obj.image and not obj.image_url:
            try:
                result = cloudinary.uploader.upload(obj.image.file)
                obj.image_url = result['secure_url']
                obj.image = None
            except Exception as e:
                print(f'Cloudinary upload error: {e}')
        super().save_model(request, obj, form, change)