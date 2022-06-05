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

 