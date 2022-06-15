from django.test import TestCase
from .models import Post, Profile
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(username='lola')
        self.user.save()
        self.profile=Profile(user=self.user,name='rish',bio='yolo.',profile_pic='default.png')
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_saveProfile(self):
        self.profile.save_profile()
        profile_saved = Profile.objects.all()
        self.assertTrue(len(profile_saved) > 0)
class PostTestClass(TestCase):
    def setUp(self):
        self.user=User(username='petr')
        self.user.save()
        self.profile=Profile(user=self.user,name='john',bio='i am funny',profile_pic='default.png')
        self.post=Post(id=1,image='default.png',title='adventure',description='A beautiful place.',user=self.profile)
    def tearDown(self):

        Post.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))
    def test_save_post(self):
        saved_post=Post.objects.all().delete()
        self.assertTrue((len(saved_post))>0)
    def test_delete_post(self):
        self.post.delete_post()
        deleted_post = Post.objects.all()
        self.assertTrue(len(deleted_post)==0)