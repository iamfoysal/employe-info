from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    full_name = models.CharField(max_length=80)
    emp_id = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete= models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
