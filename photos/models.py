from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

 
User = get_user_model() 
# Create your models here.
class Category (models.Model):
     name = models.CharField(max_length=100, null=False,blank=False)
  
def __str__ (self):
      return self.name
 
class Photo (models.Model):
     category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
     image = CloudinaryField('image')
     description = models.TextField()
     submission_url = models.TextField()
     
def __str__ (self):
      return self.description 
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile')
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    email_address = models.EmailField(max_length=150,blank=True)
    profileimg = CloudinaryField(default='https://res.cloudinary.com/dc6ecphjr/image/upload/v1654980533/blank-profile-picture_jitpja.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username