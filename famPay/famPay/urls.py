from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.models import User


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("youtube.urls", "youtube"), namespace="youtube")),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
