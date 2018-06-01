from django.db import models


# Create your models here.

class sample_model(models.Model):
    objects = None
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self):
        return self.first_name