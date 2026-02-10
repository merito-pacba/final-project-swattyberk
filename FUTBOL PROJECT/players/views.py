from django.shortcuts import render
from .models import Player  # Oyuncu modelini içeri aktarıyoruz

def home(request):
    # Veritabanındaki tüm oyuncuları çekiyoruz
    players = Player.objects.all() 
    # Bu oyuncuları 'index.html' sayfasına gönderiyoruz
    return render(request, 'index.html', {'players': players})