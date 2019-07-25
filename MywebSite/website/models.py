from django.db import models


class Projet(models.Model):
    image = models.ImageField()
    name_url = models.URLField()
    category = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name_url