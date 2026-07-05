from django.contrib import admin
from .models import Photographer, Client, Gallery, GalleryCategory, Photo

# Register your models here.

@admin.register(Photographer)
class PhotographerAdmin(admin.ModelAdmin):
    list_display = ("business_name", "user", "phone")

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("user", "phone")

class GalleryCategoryInline(admin.TabularInline):
    model = GalleryCategory
    extra = 1

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "client", "photographer", "event_date", "created_at")
    inlines = [GalleryCategoryInline, PhotoInline]

@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "gallery", "order")

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "gallery", "category", "uploaded_at")
