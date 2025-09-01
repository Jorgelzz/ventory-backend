from django.db import models


# Create your models here.
class Location(models.TextChoices):
    ZERO_A = "0-A", "0-A"
    ONE_A = "1-A", "1-A"
    TWO_A = "2-A", "2-A"
    THREE_A = "3-A", "3-A"
    FOUR_A = "4-A", "4-A"
    ZERO_B = "0-B", "0-B"
    ONE_B = "1-B", "1-B"
    TWO_B = "2-B", "2-B"
    THREE_B = "3-B", "3-B"
    FOUR_B = "4-B", "4-B"


class MovementType(models.TextChoices):
    ENTRY = "entry", "Entry"
    EXIT = "exit", "Exit"


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.username} | {self.email}"


class Product(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    localization = models.CharField(
        max_length=10, choices=Location.choices, default=Location.ZERO_A
    )
    quantity = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.product_name} | {self.localization} : {self.quantity}"


class InventoryManagement(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10, choices=MovementType.choices, default=MovementType.ENTRY
    )
    localization = models.CharField(
        max_length=10, choices=Location.choices, default=Location.ZERO_A
    )
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.product} | {self.status}: {self.quantity}"

