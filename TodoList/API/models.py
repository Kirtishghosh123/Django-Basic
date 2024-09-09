from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    age = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.name
    
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title