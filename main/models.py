from distutils.command.upload import upload
from django.db import models
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Creations(models.Model):
    def __str__(self):
        return f'{self.titre}'
    cree_a = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=os.path.join(BASE_DIR, 'images/'),width_field=None, height_field=None)
    titre = models.fields.TextField(max_length=50)
    description = models.fields.TextField(max_length=1000)
