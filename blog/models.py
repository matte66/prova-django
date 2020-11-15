from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from django.utils import timezone

from provaDjango import settings


class Post(models.Model):
    autore = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # chiave primaria
    titolo = models.CharField(max_length=200)  # parametro con lunghezza massima 200 caratteri
    testo = models.TextField()  # area di testo
    creaData = models.DateTimeField(default=timezone.now)
    pubblicaData = models.DateTimeField(blank=True, null=True)


    def pubblica(self):
        self.pubblicaData = timezone.now()
        self.save()

    def __str__(self):
        return self.titolo
