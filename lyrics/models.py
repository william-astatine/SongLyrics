from django.db import models


class Lyric(models.Model):
    name = models.CharField(max_length=255, null=True)
    artist = models.CharField(max_length=255, null=True)
    lyric = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} by {self.artist}"
    



class Artist(models.Model):
    name = models.CharField(max_length=100, null=True)
