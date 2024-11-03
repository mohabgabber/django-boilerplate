from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("landing.urls")),
    path("api/", include("api.urls")),
    path("management/", include("management.urls")),
    path("task/", include("tasks.urls")),
    path("users/", include("users.urls")),
]
