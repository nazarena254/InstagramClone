from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import cloudinary

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name=models.CharField(max_length=50)
    bio=models.TextField(max_length=500,blank=True)
    # profile_pic=models.ImageField(upload_to='pictures/',default='default.png')
    # profile_pic=cloudinary.models.CloudinaryField('image')
    profile_pic=CloudinaryField('image')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    # signals help decoupled applications to
    # get notified when actions occur elsewhere in the framework
    # pre_save/post_save mthds are sent before or after a model’s save() method is called.
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()
    def __str__(self):
        return f'{self.user.username} Profile'

class Post(models.Model): 
    #image = models.ImageField(upload_to='posts/')
    # image = cloudinary.models.CloudinaryField('image')
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def save_post(self):
        # Method to save images
        self.save()

    def delete_post(self):
        # Method to delete our images
        self.delete()
   
    def num_liked(self):
        # Method to count likes
        return self.likes.count()
   
    class Meta:
        # Class method to display images by date published
        ordering = ["-pk"]
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(Profile,related_name='comments',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(post__id=id)
        return comments

    def __str__(self):
        return self.comment
    class Meta:
        ordering=["-pk"]

class Follow(models.Model):
    follower=models.ForeignKey(Profile,related_name='followers',on_delete=models.CASCADE)
    followed=models.ForeignKey(Profile,related_name='followed',on_delete=models.CASCADE)

    def __str__(self):
        return self.follower

