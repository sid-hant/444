from django.db import models
from django.contrib.auth import get_user_model
from timing.models import PhilDay

User = get_user_model()
# Create your models here.

class StaffSchedule(models.Model):
    staffID = models.ForeignKey(User, related_name="staffUserID", on_delete=models.CASCADE)
    day = models.ForeignKey(PhilDay, related_name="philDay", on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.staffID, self.day)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)