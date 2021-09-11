from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

"""creating router to extend the url path with classes"""
router = DefaultRouter()
router.register("video", views.videoViewSet, basename="youtube")

urlpatterns = router.urls
urlpatterns += [path("search", views.searchListView.as_view())]
