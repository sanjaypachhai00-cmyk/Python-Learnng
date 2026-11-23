from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    age = models.IntegerField(default=18)

    course = models.CharField(
        max_length=100,
        blank=True
    )

    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name