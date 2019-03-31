from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class PhilDay(models.Model):
    startDay = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    endDay = models.DateField()

    def __str__(self):
       return "{}".format(self.startDay)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ArrivalTime(models.Model):
    licenseID = models.ForeignKey(User, related_name="userID", on_delete=models.CASCADE)
    philsDay = models.ForeignKey(PhilDay, related_name="dayPhils", on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
       return "{} - {}".format(self.licenseID, self.philsDay)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)