from django.db import models

# Create your models here.
class Who(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName

class Task(models.Model):
    title = models.CharField(max_length=50)
    who = models.ForeignKey(Who, on_delete=models.CASCADE)
    description = models.TextField()
    dateToFinish = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title