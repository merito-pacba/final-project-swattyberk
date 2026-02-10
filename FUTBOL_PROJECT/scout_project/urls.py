from django.contrib import admin
from django.urls import path
from players import views # Uygulama adın players olduğu için

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # views içindeki home fonksiyonuna bağladık
]