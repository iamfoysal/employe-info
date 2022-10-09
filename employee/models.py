from django.db import models



class Position(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.title


class Gender(models.Model):
    g_type=(
    ( "Male" , "Male"),
    ( "Female" , "Female"),
    ( "Other's" , "Other's")

    )
    gender = models.CharField(choices = g_type, max_length=50, null=True, blank=True)
    def __str__(self):
        return self.gender


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100, null=True, blank=True)
    mothers_name = models.CharField(max_length=100, null=True, blank=True)
    emp_id = models.CharField(max_length=20,null=True, blank=True)
    position = models.ForeignKey(Position,on_delete= models.CASCADE, null=True, blank=True)
    join_date = models.DateField(null=True, blank=True,)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=255,null=True, blank=True)
    gender = models.ForeignKey(Gender,on_delete= models.CASCADE, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=5000, null=True, blank=True)
    description = models.TextField(max_length=5000,null=True, blank=True )
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.full_name

