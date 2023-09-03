from django.db import models
from django.utils.text import slugify


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Category, self).save(*args, **kwargs)


class Sneakers(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField()
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    character = models.TextField()
    UZ = "so'm"
    USD = "$"
    RUB = "₽"
    the_price = (
        (UZ, "so'm"),
        (USD, "$"),
        (RUB, "₽"),
    )
    price_type = models.CharField(max_length=128, choices=the_price, default="so'm")
    price = models.IntegerField()


class Buy(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    product = models.ForeignKey(Sneakers, on_delete=models.CASCADE, null=True)
    all_size = (
        ("35", "35"),
        ("36", "36"),
        ("37", "37"),
        ("38", "38"),
        ("39", "39"),
        ("40", "40"),
        ("41", "41"),
    )
    size = models.CharField(max_length=100, choices=all_size)
    all_values = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    how = models.CharField(max_length=100, choices=all_values)
    map = models.TextField()
    email = models.EmailField(blank=True)



class Advertising(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    image = models.ImageField()

