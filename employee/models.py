from django.db import models

class Employee(models.Model):   
    name = models.CharField(max_length=50)  
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

    
