from django.db import models


class video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=10000)
    publishing_time = models.DateTimeField()

    def __str__(self):
        return self.title


class thumbnailURL(models.Model):
    video = models.ForeignKey(video,on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
# Create your models here.
