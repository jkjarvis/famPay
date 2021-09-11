from django.db import models


"""Storing the video title, description and publishing_time"""


class video(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(max_length=10000)
    publishing_time = models.DateTimeField()

    def __str__(self):
        return self.title


"""Storing the thumbnail URLs with key refering to respective videos"""


class thumbnailURL(models.Model):
    video = models.ForeignKey(video, on_delete=models.CASCADE)
    url = models.URLField(max_length=500)
