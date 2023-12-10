from django.db import models

# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    genre=models.CharField(max_length=20)
    language=models.CharField(max_length=20)

    def __str__(self):
        return self.title