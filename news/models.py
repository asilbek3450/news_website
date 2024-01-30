from django.db import models
from django.utils.text import slugify
from accounts.models import User


# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=128)
    category_id = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    description = models.TextField()

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_cover_image(self):
        cover_image = NewsImage.objects.filter(news=self).first()
        return cover_image

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    news_id = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def get_user(self):
        user = User.objects.get(id=self.user_id)
        return user.first_name + ' ' + user.last_name

    def __str__(self):
        return self.comment_text
