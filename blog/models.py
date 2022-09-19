from datetime import datetime
from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField(datetime.date.today())
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title
