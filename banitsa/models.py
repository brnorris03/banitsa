from django.db import models


class Fortune(models.Model):
    fortune_text = models.CharField(max_length=1000)
    english_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
