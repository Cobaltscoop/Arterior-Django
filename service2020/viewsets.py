from rest_framework import viewsets
from .serializers import ArtistSerializer, AssistantSerializer, GallerySerializer, StoreSerializer
from .models import Artist, Assistant, Gallery, Store


# Restful API View Functions
## https://butter-shower.tistory.com/51

class ArtistView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
