from django.db import models
from django.urls import reverse

class Schedule(models.Model):
    topic  = models.TextField(max_length = 200)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):   # it will redirect us to our newly saved blog post (will show its title and description)
        return reverse('schedule_detail', args = [str(self.id)])