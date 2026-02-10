from django.contrib import admin
from django.urls import path
from django.conf import settings # Bunu ekle
from django.conf.urls.static import static # Bunu ekle
from players import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Bu satırı ekle