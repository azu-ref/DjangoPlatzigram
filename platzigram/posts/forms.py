"""Posts Forms"""

#django
from django.forms import ModelForm

#Models
from posts.models import Post

class PostForm(ModelForm):
    """post model form"""

    class Meta:
        """form settings"""
        model = Post
        fields = ('user', 'profile', 'title', 'photo')