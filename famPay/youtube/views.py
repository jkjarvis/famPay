from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import video, thumbnailURL
from .serializers import videoSerializer, thumbnailSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import generics
import requests
import json
from rest_framework import filters

class videoViewSet(viewsets.ModelViewSet):
    serializer_class = videoSerializer
    queryset = video.objects.all()



    # @action(methods=["GET"], detail=True, url_name="search", url_path="search")
    def upload(self,request,pk=None):
        url = 'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&q=cricket&key=AIzaSyB5Kr212duSycZJWM-zXg5A_7tDV-CquIg'

        response = requests.get(url)
        response = response.json()['items'][0]['snippet']
        title = response['title']
        description = response['description']
        publishing_time = response['publishTime']

        video = video.objects.create(title=title,description=description,publishing_time=publishing_time)

        for i in response['thumbnails'].values():
            thumbnailURL.objects.create(video=video,url=i['url'])

        return Response(
            {'title': title,
             'description': description,
             'publishing_time': publishing_time}
        )
    

    # @action(methods=["GET"], detail=True, url_name="videos", url_path="videos")
    def list(self,request,pk=None):
        queryset = video.objects.all().order_by('-publishing_time')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # @action(detail=True, methods=['GET'], url_name="search", url_path='search')
    # def search(self,request,pk=None):
    #     title=request.data['title']
    #     description=request.data['description']
    #     print('reach')
    #     queryset = video.objects.filter(title__icontains=title,description__icontains=description)

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)


class searchListView(generics.ListAPIView):
    queryset = video.objects.all()
    serializer_class = videoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description',]


        

        



# Create your views here.
