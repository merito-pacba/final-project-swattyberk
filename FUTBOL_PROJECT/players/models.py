from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='player_pics/')
    position = models.CharField(max_length=50) # Mevki (Pos)
    team = models.CharField(max_length=100)     # Takım (Squad)
    age = models.IntegerField()                # Yaş (Age)
    goals = models.IntegerField(default=0)     # Gol (Gls)
    assists = models.IntegerField(default=0)   # Asist (Ast)
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def __str__(self):
        return self.name