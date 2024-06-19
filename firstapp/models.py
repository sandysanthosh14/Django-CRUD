from django.db import models

class Bio (models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=40)
