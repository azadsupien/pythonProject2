from django.db import models


# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    decsription = models.CharField(max_length=200, blank=False)


def __str__(self):
    return self.title


