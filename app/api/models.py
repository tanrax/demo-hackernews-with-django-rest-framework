from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=500)
    votes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
