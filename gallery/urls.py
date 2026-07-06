from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("prijava/", auth_views.LoginView.as_view(template_name="gallery/login.html"), name="login"),
    path("odjava/", auth_views.LogoutView.as_view(), name="logout"),
    path("moja-galerija/", views.moja_galerija, name="moja_galerija"),
    path("", RedirectView.as_view(pattern_name="moja_galerija"), name="pocetna"),
]