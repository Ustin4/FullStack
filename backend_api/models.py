from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
