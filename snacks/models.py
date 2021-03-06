from django.db import models
from django.contrib.auth import get_user_model
# from django.db.models.fields import CharField

# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(default='')
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
