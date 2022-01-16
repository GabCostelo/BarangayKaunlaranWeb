from django.db import models
from datetime import date, time
from django.urls import reverse

# Create your models here.
class PostEvent(models.Model):
    title = models.CharField(max_length=255)
    Place = models.CharField(max_length=255)
    postingDate = models.DateField(auto_now_add=True)
    Date = models.DateField()
    Time = models.TimeField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post:postDetail',kwargs={'pk':self.pk})
