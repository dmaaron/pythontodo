from django.db import models

# Create your models here.
class Task(models.Model):
    description=models.CharField(max_length=140)

    def __unicode__(self):
        return self.description
