from django.contrib import admin
from article.models import Article
# Register your models here.
#注册Article 到admin中

admin.site.register(Article)