from django.db import router
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView
from .views import homeViewIndex, storeDetail, GalleryView, storeList, testView

app_name = 'service2020'
urlpatterns = [
    path("", homeViewIndex, name="home"),
    path("store/", storeList, name="list"),
    path("store/<str:slug>/", storeDetail, name="slug"),
    path("gallery/", GalleryView.as_view(), name="gallery"),
    # path("test/", testView, name="test"),
]



# https://www.django-rest-framework.org/api-guide/routers/
# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# urlpatterns = [
    # path("store/", StoreListView.as_view(), name="list"),
    # path("store/<str:slug>/", StoreDetailView.as_view(), name="slug"),
    # path("about/", AboutView.as_view(), name="about"),
# ]
# urlpatterns += router.urls



# Cache Setting ..
# 하지만 Nginx 에서 Cache 설정하는 방법이 더 효과적... 
# 때문에 딱히 필요는 없는 기능이다 ㅠ..

# Django Cache Setting
# https://testdriven.io/blog/django-caching/
# =========================================================
# from django.views.decorators.cache import cache_page
# path("", cache_page(60 * 15)(homeViewIndex), name="home"),
