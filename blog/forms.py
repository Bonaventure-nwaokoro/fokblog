from .models import Post, Comment
from django.forms import ModelForm

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)