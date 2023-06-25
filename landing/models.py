from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    photo = models.ImageField()
    category = models.ForeignKey('landing.Category', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    full_name = models.CharField(max_length=255)
    number = models.IntegerField()
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.full_name} - {self.number}"


class Slide(models.Model):
    image = models.ImageField()