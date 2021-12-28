"""server URL Configuration
https://docs.djangoproject.com/en/3.1/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


from rest_framework import routers
from service2020 import viewsets

router2020 = routers.DefaultRouter()
router2020.register(r'artist2020', viewsets.ArtistView, 'artist2020')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router2020.urls, 'api_2020'), namespace='api_2020')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('main.urls', namespace='main')),
    path('y2020/', include('service2020.urls', namespace='service2020')),
    path('y2019/', include('service2019.urls', namespace='service2019')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
