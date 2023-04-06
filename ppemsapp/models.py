from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DailyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=50, blank=True, null = True)
    discription = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    


#leave 
class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cause_of_leave = models.TextField(blank=True, null=True)
    from_date = models.DateField()
    to_date = models.DateField()
    status = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    

#To-Do List

class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    what_to_do = models.TextField(blank=True, null=True)
    when_to_do = models.DateField(blank=True, null=True)
    pending_status = models.BooleanField(blank=True)
    working_status = models.BooleanField(blank=False)
    done_status = models.BooleanField(blank=False)

    def __str__(self):
        return str(self.user)