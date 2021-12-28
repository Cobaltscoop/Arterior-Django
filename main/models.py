from django.db import models
import csv

# Create your models here.

# Ajax Turorial
# https://youtu.be/jqSl36xR9Ys
# https://github.com/hellopyplane/Live-search-using-django-javascript
class Info(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return str(self.name)


class Wine(models.Model):
    country = models.CharField(max_length=100)
    designation = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    points = models.CharField(max_length=20, null=True)
    price = models.CharField(max_length=20, null=True)
    province = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=150, null=True)
    taster_name = models.CharField(max_length=120, null=True)
    title = models.CharField(max_length=200, null=True)
    variety = models.CharField(max_length=150, null=True)
    winery = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.title

    def bulk_from_csv():
        r"""CSV 파일의 정보를 DataBase 에 저장한다"""
        data_csv = open("./media/csv/wind.csv")
        data = csv.reader(data_csv)
        bulk_list = []
        for num, _ in enumerate(data):
            bulk_list.append(
                Wine(
                    country = _[0],
                    designation = _[1],
                    description = _[2],
                    points = _[3],
                    price = _[4],
                    province = _[5],
                    region = _[6],
                    taster_name = _[7],
                    title = _[8],
                    variety = _[9],
                    winery = _[10],
                )
            )
        Wine.objects.bulk_create(bulk_list)