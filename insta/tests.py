from django.test import TestCase
from .models import Profile,Post,Comment
from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(username='naz')
        self.user.save()
        self.profile=Profile(user=self.user,name='nazarena',bio='Stand tall',profile_pic='default.png')
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
        self.user=User(username='naz')
        self.user.save()
        self.profile=Profile(user=self.user,name='nazarena',bio='Stand tall',profile_pic='default.png')
        self.post=Post(id=1, likes=10, image='default.png', title='food', description='can be taken as meal or snack',user=self.profile)
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

 