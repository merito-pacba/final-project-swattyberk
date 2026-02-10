from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    team = models.CharField(max_length=100)
    rating = models.IntegerField() # 1-10 arası puan
    notes = models.TextField()
    image = models.ImageField(upload_to='player_pics/', null=True, blank=True)

    def __str__(self):
        return self.name