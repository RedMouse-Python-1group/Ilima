from django.db import models


class Article(models.Model):
    title = models.CharField(max_lenght=200)
    text = models.TextField()
    user = models.ForeignKey(User)


