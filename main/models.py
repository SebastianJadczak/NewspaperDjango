from django.db import models

class News(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(default="")
    photo = models.ImageField(null=True, blank=True, upload_to='photo')

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

