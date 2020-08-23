from django import forms
from .models import PostProblem, Comment

choices = [('critical','critical'), ('mild','mild'), ('solved','solved')]

class PostProblemForm(forms.ModelForm):
    class Meta:
        model = PostProblem
        fields = ('creator', 'problem_title', 'image', 'location', 'status')

        widgets = {
            'creator': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
            'status': forms.Select(choices=choices)
        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'content')

        widgets = {
            'user': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'})
        }
