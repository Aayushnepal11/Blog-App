from .models import BlogPost
from django import forms

class CreatePost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
