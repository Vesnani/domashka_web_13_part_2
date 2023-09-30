from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    fullname = models.CharField(max_length=100, null=False)
    born_date = models.CharField(max_length=50, null=False)
    born_location = models.CharField(max_length=100, null=False)
    description = models.TextField()

    def __str__(self):
        return self.fullname


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'user'], name='tag of username')
        ]

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    quote = models.TextField(null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.quote}"

class MyModel(models.Model):
    data = models.JSONField(null=True)

    def __str__(self):
        return str(self.id)