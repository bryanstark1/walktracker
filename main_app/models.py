from django.db import models

# Create your models here.
class Walk(models.Model):
    date = models.DateField()
    miles = models.DecimalField(max_digits=3, decimal_places=1)
    destination = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.date} ({self.id})'