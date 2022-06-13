from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

 
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
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
  
class Post(models.Model):
         id = models.UUIDField(primary_key=True,default=uuid.uuid4)
         user = models.CharField(max_length=100)
         image = models.ImageField(upload_to = 'post_images')
         caption = models.TextField()
         created_at = models.DateTimeField(default=datetime.now)
         
         
def __str__(self):
         return self.user
 
 