from re import M
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name}"
    
class Song(models.Model):
    title = models.CharField(max_length=50,blank=True)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}"
    
class Lyric(models.Model):
    content = models.TextField(max_length=150,blank=True)
    song_id = models.ForeignKey(Song,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.content}"
    