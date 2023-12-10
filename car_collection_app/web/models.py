from django.db import models

from car_collection_app.web.validators import year_validator


class Profile(models.Model):

    username = models.CharField(
        max_length=10,
        # validators=min_len_username_validator,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
    )
    password = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    @property
    def name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return f"{self.first_name}"
        elif self.last_name:
            return f"{self.last_name}"
        else:
            return ""


class Car(models.Model):
    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        validators=(year_validator,),
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )
