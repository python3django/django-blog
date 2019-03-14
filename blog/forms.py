from django import forms
from .models import Comment, Post

 
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {'title': forms.TextInput(attrs={'size': 60}), 'body': forms.Textarea(attrs={'rows':4, 'cols':70}),}
        labels = {'title': 'Post title', 'body': 'Post text', }

