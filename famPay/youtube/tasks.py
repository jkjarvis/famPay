from celery.schedules import crontab
from celery import shared_task
from celery.decorators import task
from celery.utils.log import get_task_logger

from famPay.celery import app
from youtube.models import video, thumbnailURL

import requests


logger = get_task_logger(__name__)

"""1.Defining the task to run with celery at regular internvals.
   2.Calling the youtube API with search query as cricket and with max 100 results
   3.Looping through the response and create video objects.
   4.Adding the thumbnail URLs related to the video"""


@app.task
def upload():
    url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&q=cricket&key=AIzaSyB5Kr212duSycZJWM-zXg5A_7tDV-CquIg"

    response = requests.get(url)
    print(response)
    response = response.json()["items"]
    for i in response:
        response = i["snippet"]
        title = response["title"]
        description = response["description"]
        publishing_time = response["publishTime"]

        v = video.objects.create(
            title=title, description=description, publishing_time=publishing_time
        )
        v.save()

        for i in response["thumbnails"].values():
            thumbnail = thumbnailURL.objects.create(video=v, url=i["url"])
            thumbnail.save()
    logger.info("Saved !!")
