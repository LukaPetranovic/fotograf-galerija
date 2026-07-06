from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def moja_galerija(request):
    galerije = request.user.client_profile.galleries.all()
    return render(request, "gallery/moja_galerija.html", {"galerije": galerije})
