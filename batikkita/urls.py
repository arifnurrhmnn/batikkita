from django.contrib import admin
from django.urls import path, include
from classification.views import *
from django.conf.urls.static import static #import folder yang ada di static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beranda, name=''),
    path('beranda/', beranda, name='beranda'),
    path('klasifikasi/', klasifikasi, name='klasifikasi'),
    path('klasifikasi/hasil_klasifikasi/', hasil_klasifikasi, name='hasil_klasifikasi'),
    path('motif_batik/', motif_batik, name='motif_batik'),
    path('motif_batik/artikel_batik/<int:id_batik>', artikel, name='artikel_batik'),
    path('tentang/', tentang, name='tentang'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
