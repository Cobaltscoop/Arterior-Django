from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Max, Min
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Artist, Assistant, Store, Gallery
import json

# Create your views here.
class GalleryView(ListView):
    model = Gallery
    template_name = "service/gallery.html"


def testView(request):
    context = {
    }
    return render(request, 'service/test.html', context)


def storeDetail(request, slug):
    item_infomation = Store.objects.get(slug=slug)
    artist_name = item_infomation.artist.name
    additional_store_names = Store.objects.filter(
        artist__name=artist_name).exclude(slug=slug)
    content = {
        'item': Store.objects.get(slug=slug),
        'storeindex': additional_store_names,
    }
    return render(request, "service/store-detail.html", content)


def storeList(request):
    total = Store.objects.all().order_by('title')
    food = Store.objects.filter(tab="음식점").order_by('title')
    restfood = Store.objects.filter(tab="휴게음식").order_by('title')
    household = Store.objects.filter(tab="생활잡화").order_by('title')
    service = Store.objects.filter(tab="서비스").order_by('title')
    context = {
        "total": total,
        "food": food,
        "restfood": restfood,
        "house": household,
        "service": service
    }
    template__name = "service/store-list.html"
    return render(request, template__name, context)


def homeViewIndex(request):
    r"""Showing the Whold dataSet in NaverMap"""
    # Get API (Store : 평균치, 전체 가게 데이터)
    lat = Store.objects.all().aggregate(Avg("latitude"))
    lat = [float(v) for _, v in lat.items()][0]
    lng = Store.objects.all().aggregate(Avg("longitude"))
    lng = [float(v) for _, v in lng.items()][0]
    center = [round(lat, 7), round(lng, 7)]

    # create the Queryset from "Python Dict"
    content_store = {}
    queryset = Store.objects.all()
    for _ in queryset:
        key_text = f"{_.title}"
        content_store[key_text] = [_.latitude, _.longitude, f"{_.slug}"]

    # Merging the Objects in Template
    content = {
        "store": json.dumps(content_store, ensure_ascii=False),
        "center": json.dumps(center),
        "artists": Artist.objects.all().order_by('name'),
        "managers": Assistant.objects.all(),
    }
    template__name = "service/home.html"
    return render(request, template__name, content)


# class HomeView(TemplateView):
#     template_name = 'example/profile.html'
#     # template_name = 'example/slide.html'
#     # template_name = 'example/health.html'


# class AboutView(ListView):
#     model = Gallery
#     template_name = "service/about.html"

# class StoreListView(ListView):
#     model = Store
#     template_name = "service/store-list.html"

class TestView(TemplateView):
    template_name = "service/store.html"
