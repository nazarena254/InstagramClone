from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Profile,Comment 

#  UserCreationForm build-in module is used to create a new user. 
# and it inherits from the ModelForm class
# ModelForm is used to generates those fields(model fields) from your model  
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    fullname=forms.CharField(max_length=254)
    # Meta class are used to avoid name clashes that way you can have a model fields
    #  in your form without that interfering with the configuration
    class Meta:
        model = User
        fields = ('username', 'fullname', 'email', 'password1','password2')
    
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image', 'title', 'description') 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post','user']
    class Meta:
        model = Comment
        fields = ('comment',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')  
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name',  'bio', 'profile_pic')