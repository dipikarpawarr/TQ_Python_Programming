from django.db import models
from django.urls import reverse

# Create your models here.
class StudentData(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    percentage = models.FloatField()
    standard = models.IntegerField()

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk':self.pk})

    class Meta:
        db_table = 'StudentData'
