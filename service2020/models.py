from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import csv
import re

# Create your models here.
FOLDER_YEAR = '2020'


class Gallery(models.Model):
    title = models.CharField(max_length=520)
    subtitle = models.CharField(max_length=50)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to=f"y{FOLDER_YEAR}/gallery",
    )
    objects = models.Manager()

    class Meta:
        ordering = ["pk"]  # ["pk", "title", "description"]

    def __str__(self) -> str:
        return f"{self.title}-{self.subtitle}"

    def bulk_from_csv():
        data = open(f"./media/y{FOLDER_YEAR}/gallery.csv")
        data = csv.reader(data)
        bulk_list = []
        for num, _ in enumerate(data):
            bulk_list.append(
                Gallery(
                    title=_[0],
                    subtitle=_[1],
                    photo=_[2],
                )
            )
        Gallery.objects.bulk_create(bulk_list)


class Assistant(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=30, blank=True)
    name_eng = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to=f"y{FOLDER_YEAR}/assistant",
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name}-{self.title}"

    def bulk_from_csv():
        file_name = f"./media/y{FOLDER_YEAR}/assistant.csv"
        data = csv.reader(open(file_name))
        bulk_list = []
        for _ in data:
            bulk_list.append(
                Assistant(
                    name=_[0],
                    email=_[1],
                    name_eng=_[2],
                    title=_[3],
                    description=_[4],
                    photo=_[5],
                )
            )
        Assistant.objects.bulk_create(bulk_list)


# Artist Table
class Artist(models.Model):
    name = models.CharField(max_length=10, unique=True)
    group = models.CharField(max_length=2)  # A, B, C Group
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    email = models.CharField(max_length=150, blank=True)
    instagram = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    blog = models.CharField(max_length=150, blank=True)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to=f"y{FOLDER_YEAR}/artist",
    )
    objects = models.Manager()

    def bulk_from_csv():
        data = open(f"./media/y{FOLDER_YEAR}/artist.csv")
        data = csv.reader(data)
        bulk_list = []
        for _ in data:
            bulk_list.append(
                Artist(
                    name=_[0],
                    group=_[1],
                    number=_[2],
                    title=_[3],
                    subtitle=_[4],
                    email=_[5],
                    instagram=_[6],
                    facebook=_[7],
                    blog=_[8],
                    photo=_[9],
                )
            )
        Artist.objects.bulk_create(bulk_list)

    class Meta:
        ordering = ["group", "number"]

    # {:02d} : only using in the Integer data
    def __str__(self) -> str:
        return f"{self.group}-{int(self.number):02d} : {self.name}"


# Matching Store Table
class Store(models.Model):
    title = models.CharField(max_length=50, unique=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='stores')

    # Basic Information
    types = models.CharField(max_length=50)
    tab = models.CharField(max_length=50)
    ceoname = models.CharField(max_length=50)
    ceophone = models.CharField(max_length=50)
    addressraw = models.CharField(max_length=100)
    addressfull = models.CharField(max_length=100)
    addressroad = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    # Text Script
    textBanner = models.CharField(max_length=120)
    textTitle = models.CharField(max_length=120)
    textTitleScript = models.CharField(max_length=500)
    textContext1 = models.CharField(max_length=750)
    textContext2 = models.CharField(max_length=750)
    textContext3 = models.CharField(max_length=750)

    # Store Images
    imageBanner1 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageBanner2 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image101 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image102 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image103 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image201 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image202 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image203 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image301 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image302 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    image303 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")

    # Extra DataSet
    slug = models.SlugField(
        unique=True,
        allow_unicode=True,
        help_text="url linking key words",
    )
    objects = models.Manager()

    # ListView Link Url to DetailView Url Function : by Slug

    def get_absolute_url(self):
        return reverse("service2020:slug", kwargs={"slug": self.slug})

    def save(self, *arg, **kwargs):
        if not self.slug:
            slug_text = "".join(re.findall(r"[0-9a-Z가-힣]+", self.title))
            self.slug = slugify(slug_text)
        return super().save(*arg, **kwargs)

    def __str__(self) -> str:
        return f"{self.artist.name} : {self.title}"

    class Meta:
        ordering = ["artist", "title"]

    def bulk_from_csv():
        Store.objects.all().delete()
        data = open(f"./media/y{FOLDER_YEAR}/store.csv")
        data = csv.reader(data)
        bulk_list = []
        for _ in data:
            # Get the Primary Table Instance of Artist name..
            name_instance = Artist.objects.get(name=_[1])
            slug_text = "".join(re.findall("[0-9A-z가-힣]+", _[0]))
            bulk_list.append(
                Store(
                    title=_[0],
                    artist=name_instance,
                    types=_[2],
                    tab=_[3],
                    ceoname=_[4],
                    ceophone=_[5],
                    addressraw=_[6],
                    addressfull=_[7],
                    addressroad=_[8],
                    longitude=_[9],
                    latitude=_[10],
                    textBanner=_[11],
                    textTitle=_[12],
                    textTitleScript=_[13],
                    textContext1=_[14],
                    textContext2=_[15],
                    textContext3=_[16],
                    imageBanner1=_[17],
                    imageBanner2=_[18],
                    image101=_[19],
                    image102=_[20],
                    image103=_[21],
                    image201=_[22],
                    image202=_[23],
                    image203=_[24],
                    image301=_[25],
                    image302=_[26],
                    image303=_[27],
                    slug=slug_text,
                )
            )
        Store.objects.bulk_create(bulk_list)

    # https://velog.io/@swhybein/Django-bulkcreate%EC%9C%BC%EB%A1%9C-csv%ED%8C%8C%EC%9D%BC-%EC%98%AC%EB%A6%AC%EA%B8%B0
    # https://www.tutorialspoint.com/sqlite/sqlite_truncate_table.html
    # def drop_table():
    #     from django.db import connection
    #     cursor = connection.cursor()
    #     table_name = self.model._meta.db_table
    #     sql = "DROP TABLE %s;" % (table_name,)
    #     cursor.execute(sql)

    # r"""https://stackoverflow.com/questions/38963193/auto-populate-slug-field-django"""
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Store, self).save(*args, **kwargs)
