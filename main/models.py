from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(default="")

    class Meta:
        verbose_name_plural = "News"

