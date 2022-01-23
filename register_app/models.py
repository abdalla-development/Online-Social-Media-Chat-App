from django.db import models

# Create your models here.
class UserInfo(models.Model):
    birth_day = models.CharField(max_length=5000)  #
    gender =  models.CharField(max_length=5000) #
    phone_number = models.CharField(max_length=5000)  #
    address = models.CharField(max_length=5000) #
    city = models.CharField(max_length=5000) #
    country = models.CharField(max_length=5000)  #
    postal_code = models.CharField(max_length=5000)  #
    about_me = models.CharField(max_length=5000, null= True)  #
    friends = models.IntegerField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField()
    age = models.IntegerField()
    profile_picture = models.ImageField(upload_to = 'static/uploads/')  #'static/uploads/'
    user_id = models.CharField(max_length=5000, null= False)  #


    def __str__(self) -> str:
        return self.user_id
   
