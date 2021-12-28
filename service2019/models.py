from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import csv
import re
FOLDER_YEAR = '2019'


# Create your models here.
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
    name_eng = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=200)
    photo = models.ImageField(
        null=True,
        blank=True,
        upload_to=f"y{FOLDER_YEAR}/assistant",
    )
    objects = models.Manager()

    def __str__(self) -> str:
        return f"{self.name} : {self.name_eng}"

    def bulk_from_csv():
        file_name = f"./media/y{FOLDER_YEAR}/assistant.csv"
        data = csv.reader(open(file_name))
        bulk_list = []
        for _ in data:
            bulk_list.append(
                Assistant(
                    name=_[0],
                    name_eng=_[1],
                    description=_[2],
                    photo=_[3],
                )
            )
        Assistant.objects.bulk_create(bulk_list)


class Artist(models.Model):
    name = models.CharField(max_length=20)
    profile = models.CharField(max_length=250)
    instagram = models.CharField(max_length=150, blank=True)
    facebook = models.CharField(max_length=150, blank=True)
    naver = models.CharField(max_length=150, blank=True)
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
                    profile=_[1],
                    instagram=_[2],
                    facebook=_[3],
                    naver=_[4],
                    blog=_[5],
                    photo=_[6],
                )
            )
        Artist.objects.bulk_create(bulk_list)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]




# Matching Store Table
class Store(models.Model):
    title = models.CharField(max_length=50, unique=True)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='stores')

    # Basic Information
    addressraw = models.CharField(max_length=100)
    addressroad = models.CharField(max_length=100)
    addressfull = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()
    phone = models.CharField(max_length=50)
    openhour = models.CharField(max_length=150)

    # Text Script
    textBanner = models.CharField(max_length=250)  # Banner Text
    textContent1 = models.CharField(max_length=250)
    textContent2 = models.CharField(max_length=250)
    textContent3 = models.CharField(max_length=250)

    # Store Images
    ## Before, After
    imageBanner1 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageBanner2 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")

    # Banner,  Processer 1,2,3
    imageBanner = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageImage1 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageImage2 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageImage3 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")

    # After Photos 1,2,3
    imageAfter1 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageAfter2 = models.ImageField(
        null=True, blank=True, upload_to=f"y{FOLDER_YEAR}/store")
    imageAfter3 = models.ImageField(
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
        return reverse("service2019:slug", kwargs={"slug": self.slug})

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
                    addressraw=_[2],
                    addressroad=_[3],
                    addressfull=_[4],
                    longitude=_[5],
                    latitude=_[6],
                    phone=_[7],
                    openhour=_[8],
                    textBanner=_[9],
                    textContent1=_[10],
                    textContent2=_[11],
                    textContent3=_[12],

                    imageBanner1=_[13],
                    imageBanner2=_[14],
                    imageBanner=_[15],
                    imageImage1=_[16],
                    imageImage2=_[17],
                    imageImage3=_[18],
                    imageAfter1=_[19],
                    imageAfter2=_[20],
                    imageAfter3=_[21],
                    slug=slug_text,
                )
            )
        Store.objects.bulk_create(bulk_list)
