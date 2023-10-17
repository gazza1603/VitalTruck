from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Vehicle(models.Model):
    fleet_no = models.CharField(max_length=20)
    cost_centre = models.CharField(max_length=20)
    reg_no = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    group = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    area_available = models.CharField(max_length=100, default='not set')
    workshop_entry_time = models.DateTimeField(null=True, blank=True)

    @property
    def workshop_duration(self):
        # If the vehicle is not in workshop or the workshop_entry_time is not set, return None
        if self.status != "workshop" or self.workshop_entry_time is None:
            return None
    # Calculate duration
        current_time = timezone.now()
        duration = current_time - self.workshop_entry_time
        return duration.days


    def __str__(self):
        return self.fleet_no
