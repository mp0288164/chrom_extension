from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
