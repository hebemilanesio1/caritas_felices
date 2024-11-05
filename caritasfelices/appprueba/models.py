from django.db import models

class CampanaActiva(models.Model):
    campaign_name = models.CharField(max_length=255)
    description = models.TextField()
    campaign_image = models.ImageField(upload_to='campaign_images/')  # Asegúrate de tener configurado MEDIA_URL y MEDIA_ROOT

    def __str__(self):
        db_table = 'appprueba_campanaactiva'


