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
     user = models.CharField(max_length=100)
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
RATE_CHOICES =[
      (1,'1-Trash'),
      (2,'1-Horrible'),
      (3,'1-Terrible'),
      (4,'1-Bad'),
      (5,'1-Average'),
      (6,'1-Nice & Neat'),
      (7,'1-Good'),
      (8,'1-Very good'),
      (9,'1-Perfect'),
      (10,'1-Masterpiece'),
]
class Review(models.Model):
          user = models.ForeignKey(User, on_delete=models.CASCADE)
          category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
          created_at = models.DateTimeField(default=datetime.now)
          text = models.TextField(max_length=3000, blank=True)
          rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
          
          
def __str__(self):
      return self.user.username     
 
 
         
 