from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=50)
    family = models.ForeignKey(Family, on_delete=models.PROTECT)
    date_of_birth = models.DateTimeField(auto_now_add=True)
    healthy = models.BooleanField(default=True)
    legs = models.SmallIntegerField(default=4)

    def __str__(self):
        return self.name

