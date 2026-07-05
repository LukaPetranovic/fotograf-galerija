from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Photographer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="photographer_profile")
    business_name = models.CharField(max_length=200, blank=True, verbose_name="Naziv obrta/studija")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")

    def __str__(self):
        return self.business_name or self.user.username
    
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="client_profile")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefon")

    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
class Gallery(models.Model):
    photographer = models.ForeignKey(Photographer, on_delete=models.CASCADE, related_name="galleries")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="galleries")
    title = models.CharField(max_length=200, verbose_name="Naziv galerije")
    description = models.TextField(blank=True, verbose_name="Opis")
    event_date = models.DateField(null=True, blank=True, verbose_name="Datum događaja")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.client})"
    
class GalleryCategory(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100, verbose_name="Naziv kategorije")
    order = models.PositiveBigIntegerField(default=0, verbose_name="Redoslijed prikaza")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} ({self.gallery.title})"
    
class Photo(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos")
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="photos")
    image = models.ImageField(upload_to="gallery_photos/%Y/%m/", verbose_name="Fotografija")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto #{self.id} - {self.gallery.title}"
    
