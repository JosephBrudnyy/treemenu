from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    absolute_url = models.TextField(blank=True)
    path = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('menu', kwargs={'menu_id': self.pk})

    def __str__(self):
        return self.name
