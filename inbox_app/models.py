from django.db import models

# Create your models here.
class Messages(models.Model):
    send_to = models.CharField(max_length=500, null= False)  
    send_from =  models.CharField(max_length=500, null= False) 
    subject =  models.CharField(max_length=500) 
    message = models.CharField(max_length=5000, null= False)  


    def __str__(self) -> str:
        return self.subject