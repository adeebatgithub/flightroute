from django.db import models


class AirportModel(models.Model):
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code


class RouteModel(models.Model):
    LEFT = 1
    RIGHT = 2
    POSiTION_CHOICES = (
        (LEFT, 'left'),
        (RIGHT, 'right'),
    )

    starting = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='starting_destination')
    ending = models.ForeignKey(AirportModel, on_delete=models.CASCADE, related_name='ending_destination')
    duration = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    position = models.PositiveSmallIntegerField(choices=POSiTION_CHOICES)


