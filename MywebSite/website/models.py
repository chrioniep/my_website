from django.db import models


class Projet(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, default='')
    name_url = models.URLField()
    category = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class Skill(models.Model):
    title = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    level_number = models.IntegerField(default=0)

    def __str__(self):
        return self.title