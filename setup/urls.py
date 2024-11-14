from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from video import views

router = DefaultRouter()
router.register(r'video', views.VideoViewSet, basename='videos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
