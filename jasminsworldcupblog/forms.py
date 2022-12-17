from .models import Comment, Item, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        

