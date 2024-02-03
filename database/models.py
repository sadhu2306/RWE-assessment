from django.db import models

# Create your models here.
class Billing(models.Model):

    Name = models.CharField(max_length=100)
    Date = models.DateField(max_length=100)
    Time = models.TimeField(max_length=100)

    def __str__(self):
        return self.name