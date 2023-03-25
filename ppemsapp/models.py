from django.db import models

# Create your models here.


class DailyTask(models.Model):
    title = models.CharField(max_length=50, blank=True, null = True)
    discription = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title