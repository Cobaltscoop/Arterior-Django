from django.urls import path
from .views import InfoListView

app_name = 'main'
urlpatterns = [
    path("", InfoListView.as_view(), name="info"),
]
