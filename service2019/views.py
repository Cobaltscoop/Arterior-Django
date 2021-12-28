from typing import ContextManager
from main.models import Info
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, TemplateView
from .models import Artist, Assistant, Gallery, Store
import json


class GalleryView(ListView):
    model = Gallery
    template_name = "service/gallery.html"