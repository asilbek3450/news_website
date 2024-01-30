from django.contrib import admin
from .models import News, NewsImage, NewsCategory, Comment
# Register your models here.
admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(NewsCategory)
admin.site.register(Comment)
