from blog.models import Post
from django import forms
from django.core.exceptions import ValidationError

class Loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class Signupform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean(self):
        clean_data = super().clean()
        password = clean_data.get("password")
        password1 = clean_data.get("password1")
            
        if password != password1:
            raise ValidationError('Password doesnot match!')
    
class AddBlogform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text','image')


   

