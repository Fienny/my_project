from django import forms
from .models import Post
class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = ['heading', 'text', 'choice', 'post_date', 'post_rating',]