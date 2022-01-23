from django.db import models

# Create your models here.
class PrivateChat(models.Model):
    user_1 = models.CharField(max_length=50000, null= False)
    user_2 = models.CharField(max_length=50000, null= False)
    chat_link_name = models.CharField(max_length=500, null= False, unique= True)
    


    def __str__(self) -> str:
        return self.chat_link_name