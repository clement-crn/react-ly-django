# myapp/models.py
from django.db import models

class Test(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name