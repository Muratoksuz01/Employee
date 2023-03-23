from django.db import models

# Create your models here.

class Position(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title
class ModelEmployee(models.Model):
    full_name=models.CharField(max_length=25)
    mobile=models.IntegerField()
    emp_code=models.IntegerField()
    position=models.ForeignKey(Position,on_delete=models.CASCADE)
    def __str__(self):
        return self.full_name