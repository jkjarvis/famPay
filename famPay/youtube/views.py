from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import video, thumbnailURL
from .serializers import videoSerializer, thumbnailSerializer

from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import generics
from rest_framework import filters

import requests
import json


class videoViewSet(viewsets.ModelViewSet):
    serializer_class = videoSerializer
    queryset = video.objects.all()

    """1.Overwriting default list method to return response with descending publishing_time
       2.Adding pagination to queryset.
       3.Formatting with serializers and sending the response"""

    def list(self, request, pk=None):
        queryset = video.objects.all().order_by("-publishing_time")
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


"""Using rest_framework search filter to search for a specific keyword in title and description"""


class searchListView(generics.ListAPIView):
    queryset = video.objects.all()
    serializer_class = videoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "description",
    ]
