from django import forms
from .models import PostProblem

choices = [('critical','critical'), ('mild','mild'), ('solved','solved')]

class PostProblemForm(forms.ModelForm):
    class Meta:
        model = PostProblem
        fields = ('creator', 'problem_title', 'image', 'location', 'status')

        widgets = {

            'creator': forms.TextInput(attrs = {'class': 'form-control', 'value': '', 'id': 'author', 'type': 'hidden'}),
            # 'creator': forms.Select(attrs = {'class': 'form-control'}),
            'problem_title': forms.Textarea(attrs = {'class': 'form-control'}),
            'location': forms.TextInput(attrs = {'class': 'form-control'}),
            'status': forms.Select(choices=choices, attrs = {'class': 'form-control'})
        }
