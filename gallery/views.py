from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Gallery

# Create your views here.

@login_required
def moja_galerija(request):
    galerije = request.user.client_profile.galleries.all()
    return render(request, "gallery/moja_galerija.html", {"galerije": galerije})

@login_required
def gallery_detail(request, gallery_id):
    """
    Prikazuje jednu galeriju: kategorije (tagove) i fotografije grupirane po kategoriji.
    get_object_or_404 s filterom client=... osigurava da klijent može otvoriti
    SAMO svoju galeriju - ako promijeni broj u URL-u i pokuša pogoditi tuđi ID,
    dobit će 404 grešku umjesto tuđih fotografija.
    """
    galerija = get_object_or_404(
        Gallery, id=gallery_id, client=request.user.client_profile
    )
    kategorije = galerija.categories.all()
    return render(
        request,
        "gallery/gallery_detail.html",
        {"galerija": galerija, "kategorije": kategorije},
    )
