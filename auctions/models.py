from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Auction(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'media')
    # , blank = True
    BIKE_TYPE = [
        ("TOU", "Touring"),
        ("MTB", "MTB"),
        ("ROA", "Road"),
        ("URB", "Urban"),
        ("BMX", "BMX"),
        ("ELE", "Electric"),
        ("OTH", "Other"),
    ]
    production_date = models.DateField()
    bike_type = models.CharField(max_length=3, choices=BIKE_TYPE)
    color = models.CharField(max_length=10)
    gears = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(40)])
    size = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.auction.title}"

