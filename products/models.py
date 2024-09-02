from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    Fruit = "F"
    Vegetable = "V"
    Meat = "M"
    Other = "O"
    CATEGORY_CHOICES = [
        (Fruit, "Fruit"),
        (Vegetable, "Vegetable"),
        (Meat, "Meat"),
        (Other, "Other"),
    ]
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name