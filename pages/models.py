from django.db import models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twitter_link = models.URLField(max_length=100)
    google_plus_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    @property
    def thumbnail_preview(self):
        if self.photo:
            _thumbnail = get_thumbnail(self.photo,
                                   '50x50',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}" style="border-radius:50%;">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    def __str__(self):
        return self.first_name
    