from django.db import models

# Create your models here.
class MotifBatik(models.Model):
    nama = models.CharField(max_length=100)
    gambar = models.ImageField(upload_to='gambar-batik/')
    artikel = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama