from django.db import models
from django.urls import reverse

class Schedule(models.Model):
    topic  = models.TextField(max_length = 200)

    def __str__(self):
        return self.topic
