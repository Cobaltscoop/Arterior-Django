# Django with Webpack

![Django badge](https://img.shields.io/badge/Django-3.1-blue.svg)
![Django badge](https://img.shields.io/badge/Python-3.8-blue.svg)

<strike>관악 아트테리어 Django 버젼으로 현재 업데이트가 중지 되었습니다.
(since 2020 may..)</strike>

<br/>

## Arterior 사이트 모델의 재정의
1. 연도별 보여지는 Main Page 별도제작 및 연도별 누적 가능한 형태로 재 조정
2. 현재 데이터 및 구조를 연도별 재 구조화 및 조직화 작업
3. 현재 자료들 2020 년 구분된 형태로 재조직화
4. 2019년 자료들의 DB 구축 및 단순한 Template 시연하기
5. 2019년 맞춤형 Template 작업의 진행

<br/>

## Django Ajax ORM 구현하기

**[Dynamically filter queryset with AJAX and DRF](https://djangopy.org/learn/dynamically-filter-queryset-with-ajax-and-drf/)**

**[Django 3.1 Ajax](https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.HttpRequest.is_ajax)**

**[Django Ajax 3.1 Changed](https://www.brennantymrak.com/articles/fetching-data-with-ajax-and-django.html)**

**[Django 검색기능 구현시 핵심정리](https://equus3144.medium.com/django%EB%A1%9C-%EA%B2%80%EC%83%89-%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4-%EB%95%8C%EC%9D%98-%ED%95%B5%EC%8B%AC-orm-filter-567be01021c5)**


### Table 을 수동으로 삭제하는 경우

**[dJango - migrate 했는데 'No migrations to apply' 일 경우!](https://velog.io/@haileeyu21/Error-dJango-migrate-%ED%96%88%EB%8A%94%EB%8D%B0-No-migrations-to-apply-%EC%9D%BC-%EA%B2%BD%EC%9A%B0)** 의 내용을 참고한 자료 입니다.

내용은 migration 파일 이름이 동일하면 별도 검사를 진행하지 않고서 작업을 실행하지 않는 문제가 발생 합니다. 단순히 폴더만 삭제하는 경우에는 Migration 파일은 다르지만 동일한 파일이름이 중복 생성되어 별도 검사를 진행하지 않고 Passing 하는 만큼, 필요에 따라 직전 파일 내부에 수동으로 삭제한 내용을 주석처리한 뒤, 새롭게 Makemigraion 을 실행하면 원하는 결과를 얻을 수 있습니다.


<br/>

## PSQL with Django

[![Django | Using a PostgreSQL Database](https://i.ytimg.com/vi/73WbBMnqPpg/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLA73qyLWFPLR3HsWYnvvDKHDdR8Sw)](https://youtu.be/73WbBMnqPpg)


## Cobalt Site 만들기

[![Responsive Resume Cv Website | Light/Dark Theme](https://i.ytimg.com/vi/oYjseP_Qhv4/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBePeqgonhP7Q2U0p3zvsr2c26aFA)](https://youtu.be/oYjseP_Qhv4)

<br/>

## Cache Setting

Nginx 에서 Cache 를 사용하도록 설정을 해 보겠습니다.

https://www.nginx.com/blog/nginx-caching-guide/

```r
$ nvim /etc/nginx/sites-enabled/default
$ nginx -t                             
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**[django-nginx-static-file-caching](https://stackoverflow.com/questions/27497472/django-nginx-static-file-caching-on-browser)** 을 참고 합니다.

https://jojoldu.tistory.com/60

https://www.joinc.co.kr/w/man/12/nginx/static

https://stackoverflow.com/questions/27508683/django-nginx-browser-caching-configuration

https://testdriven.io/blog/django-caching/



- **[Full Screen to the Image](https://stackoverflow.com/questions/37753753/full-screen-image-when-clicked/37754029)**

- Reveal.js : https://dymaxionkim.github.io/beautiful-jekyll/2017-01-25-Revealjs/

- Reveal.js : https://revealjs.com/layout/

- stick.js : http://kenwheeler.github.io/slick/

## AOS with Preloader

from the [Stack Over the Flow](https://stackoverflow.com/questions/65881788/aos-animate-on-scroll-js-not-working-while-implementing-css-preloader)

```
```



## Slider : slick.js

https://whiumisc.tistory.com/77


## Loading Spinner

- **[How to show Page Loading div until the page has finished loading?](https://www.geeksforgeeks.org/how-to-show-page-loading-div-until-the-page-has-finished-loading/)**

Naver Map 및 이미지들을 여러개 불러오다 보니 Loading Page 처리를 해야할 필요가 생겼습니다. Django 의 별도 redirect 방식을 활용하기 보다는, HTML CSS JavaScript 의 기본 문법을 활용하는 방법이 가장 효과적 이었습니다.

[StackOverFlow](https://stackoverflow.com/questions/25253391/javascript-loading-screen-while-page-loads) 와 [Youtube](https://youtu.be/xuA83OYTE7I) 동영상의 내용을 참고로 작업 하였습니다.

- **[How To Create A Custom Preloading Screen](https://ihatetomatoes.net/create-custom-preloading-screen/)**

```javascript
```

<br/>

## Exif Transition

jpg 에는 META 값으로 **[Exif (교환 이미지 파일 형식)](https://namu.wiki/w/EXIF)** 를 표준으로 포함하고 있습니다. 이 정보 중 **회전** 값이 문제가 되는데, HTML 에서는 기본 이미지를 중심으로 변환을 하다 보니 **object-fit** 값이 **Cover** 임에도 사진이 외곡 되는 문제가 발생하였습니다.

이를 해결하는 방법으로 **[exiftran](http://manpages.ubuntu.com/manpages/precise/man1/exiftran.1.html)** 를 활용하여 Meta 값으로 사진을 회전한 상태로 변환을 하여 저장하였고, 이후 이러한 문제는 해결 되었습니다.

```r
$ sudo apt-get install -y exiftran
$ exiftran -ai *.jpg
```

<br/>

## Source DataBase

- **[아트테리어 가게 DB 목록용 Sheet](https://docs.google.com/spreadsheets/d/15BjMq9NOaalGWh0ffyUcjIMiyJta-VZxfNkPSNgeK3E/edit#gid=942529316)**

- **[아트테리어 지리명 정리 Sheet](https://docs.google.com/spreadsheets/d/15UCP9IGTDJ7Gmneyxm41WOYfZ7pkdvZDzpcyAn3zBkI/edit#gid=1381188533)**

<br/>

## Work Place

- **[Figma Sketch](https://www.figma.com/file/IGA5vV06ufcOTRKkBAb50h/Untitled?node-id=168%3A2342)**

- **[Artist and Store Detail DataSheet](https://docs.google.com/spreadsheets/d/15BjMq9NOaalGWh0ffyUcjIMiyJta-VZxfNkPSNgeK3E/edit?pli=1#gid=0)**

- **[Naver Map 개발문서](https://navermaps.github.io/maps.js.ncp/docs/tutorial-2-Getting-Started.html)**

<br/>

## HTML & CSS Tips

- **[How to use as Image as a link in HTML](https://www.tutorialspoint.com/How-to-use-an-image-as-a-link-in-HTML)**

<br/>

## Django Tips

### VS CODE extension Backup & Restore

```r
On the old machine:

$ code --list-extensions > vscode-extensions.list

On the new machine:

$ cat vscode-extensions.list | xargs -L 1 code --install-extensio
```

from the [StackOverFlow](https://stackoverflow.com/questions/35773299/how-can-you-export-the-visual-studio-code-extension-list/49936683#49936683)


### Extend vs Include

html 태그에서 아래의 내용을 혼동하여 사용하면 Delay 가 생기는 문제가 발생한다. 따라서 해당 태그들의 차이를 알고 사용하자

- Extend "base.html" : Template (base.html) 에서 확장하여 내용들을 추가하는 템플릿 함수로, 맨 위에서 추가 된다

- Include "footer.html" : 원본 Template 에서 (footer.html) 을 추가하는 함수로 탬플릿 사이 사이에서 활용 된다

### Creating the parent folder in Ubuntu

```r
$ mkdir -p static/{js,css}
```

Linking the Static files, using for CSS Peak

```html
<link rel="stylesheet" href="/static/css/style.css">
<img src="/media/face3.jpg" alt="">
```

webpack install 

```r
$ yarn add webpack webpack-cli webpack-dev-server
$ yarn add -D style-loader css-loader
$ yarn add -D @babel/core @babel/preset-env @babel/preset-react @babel/plugin-proposal-class-properties
```

https://studiomeal.com/archives/533

**[Animate On Scroll Library](https://michalsnik.github.io/aos/)**

<br/>

## Additional Links

- **[Python jedi Error in Ipython](https://github.com/ipython/ipython/issues/12740)**

- **[Django: get data from tables and display together using ListView](https://stackoverflow.com/questions/56515279/django-get-data-from-tables-and-display-together-using-listview)**

- **[Django DetailView get_context_data](https://stackoverflow.com/questions/45679155/django-detailview-get-context-data)**

- **[Django's static to set a background image](https://simpleit.rocks/python/django/call-static-templatetag-for-background-image-in-css/)**

- **[Figma Sketch](https://www.figma.com/file/IGA5vV06ufcOTRKkBAb50h/Untitled?node-id=168%3A2342)**

- **[Artist and Store Detail DataSheet](https://docs.google.com/spreadsheets/d/15BjMq9NOaalGWh0ffyUcjIMiyJta-VZxfNkPSNgeK3E/edit?pli=1#gid=0)**lete guide to webpack 5 (2020)](https://www.valentinog.com/blog/webpack/)**

<br/>

## Django Query Set

- filter Query Set

```python
In : item = Store.objects.get(slug="선녀와나무꾼")
In : item.artist.name
Out : '최윤혜'

In: Store.objects.filter(artist__name="최윤혜")
Out: <QuerySet [<Store: 최윤혜 : 뚱띵이왕갈비>, 
<Store: 최윤혜 : 선녀와 나무꾼>,
<Store: 최윤혜 : 육교식당>, 
<Store: 최윤혜 : 장수우렁불백>]>

In: Store.objects.filter(artist__name="최윤혜").exclude(slug="선녀와나무꾼")
Out: <QuerySet [<Store: 최윤혜 : 뚱띵이왕갈비>, 
<Store: 최윤혜 : 육교식당>, 
<Store: 최윤혜 : 장수우렁불백>]>
```

- Back Reference Query Set

객체를 참조하는 경우, Foreign Field 에서는 'file name' 이름으로 바로 호출이 가능하다 

```python
Store.objects.filter(artist__name="최윤혜").exclude(slug="선녀와나무꾼")
```

역참조(Back Reference) 는 Primary Field 에서, 이를 상속받는 Table 의 값을 불러오기 위한 방법인데, 참조하는 테이블이 많을수록 이를 연결하기가 까다롭다는 문제점이 생깁니다.

이러한 문제를 해결하기 위해서 `Models.py` 에서 `Field` 를 정의할 때 `related_name` 속성값을 사용하면, 해당 **이름 값** 을 사용하면 참조하는 테이블의 값을 shell, Template 모두에서 바로 가져올 수 있습니다.

```python
# models.py
# Matching Store Table
class Store(models.Model):
    artist = models.ForeignKey(Artist, related_name='stores')

In [1]: test = Artist.objects.first()
In [2]: test.stores.all()
Out[2]: <QuerySet [<Store: 박현철 : 김현애보습학원>, <Store: 박현철 : 영진떡방앗간>, <Store: 박현철 : 영진부동산>, <Store: 박현철 : 카페네온>]>
```

```html
{% raw %}
<div class="container">
  {% for people in artist %}            
    {% for store in people.stores.all %}
      <a href="{{ store.get_absolute_url }}">- {{ store.title }}</a>
    {% endfor %}
  {% endfor %}
</div>
{% endraw %}
```


