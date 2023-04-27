from django import forms
from .commentModel import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Comment
        fields = ['text']
