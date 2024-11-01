from django.db import models # type: ignore

class Document(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    position = models.IntegerField()

    def __str__(self):
        return self.title
