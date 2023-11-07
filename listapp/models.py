from django.db import models

# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.Title
    