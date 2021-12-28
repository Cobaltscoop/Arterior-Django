from django.urls import path
from .views import GalleryView

app_name = 'service2019'
urlpatterns = [
    path("gallery/", GalleryView.as_view(), name="gallery"),
    # path('')
]
