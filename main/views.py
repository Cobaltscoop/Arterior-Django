from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from django.template.loader import render_to_string
from django.http import JsonResponse
from rest_framework import pagination
from .models import Info
import json
# Create your views here.

# 아랫 내용으로 새롭게 작업 해보기
# https://djangopy.org/learn/dynamically-filter-queryset-with-ajax-and-drf/
class InfoListView(ListView):
    model = Info
    template_name = "main/ajax.html"

    # Generic View 에서 사용된 Context Data 를 호출하는 함수
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs_json"] = json.dumps(list(Info.objects.values()))
        return context


# Django 에서 Ajax 실습
# https://equus3144.medium.com/django%EB%A1%9C-%EA%B2%80%EC%83%89-%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4-%EB%95%8C%EC%9D%98-%ED%95%B5%EC%8B%AC-orm-filter-567be01021c5
def home(request):
    url_parameter = request.GET.get("q", None)
    if url_parameter:
        results = Info.objects.filter(name__icontains=url_parameter)
    else:
        results = Info.objects.all()

    # if request.is_ajax():
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string(
            template_name = "main/result.html",
            context = {"results": results},
        )
        data_dict = {
            "html_from_view": html
        }
        return JsonResponse(data=data_dict, safe=False)
    return render(request, "main/home.html", {"results": results})



# Wind 데이터를 활용한 Restful API 및 Ajax 실습
# https://djangopy.org/learn/dynamically-filter-queryset-with-ajax-and-drf/
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import WineSerializers
from .models import Wine
from .pagination import StandardResultsPagination


def windList(request):
    context = {}
    return render(request, 'main/wine.html', context)


class WineListing(ListAPIView):
    pagination_class = StandardResultsPagination
    serializer_class = WineSerializers

    def get_queryset(self):
        queryList = Wine.objects.all()
        country = self.request.query_params.get('country', None)
        country = self.request.query_params.get('country', None)
        country = self.request.query_params.get('country', None)
        country = self.request.query_params.get('country', None)
        country = self.request.query_params.get('country', None)
        country = self.request.query_params.get('country', None)
