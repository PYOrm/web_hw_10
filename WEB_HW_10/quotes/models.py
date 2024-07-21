from django.db import models


# Create your models here.
class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.DateField()
    born_location = models.CharField(max_length=200)
    description = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Quote(models.Model):
    qoute = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


