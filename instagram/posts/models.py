from django.db import models

# Create your models here.
from django.db import models


class Posts(models.Model):
    created = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    description = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")
    img = models.CharField(max_length=500, unique=False, blank=True, null=False, default="")