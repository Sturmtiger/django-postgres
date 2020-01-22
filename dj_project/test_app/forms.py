from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name', 'message')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
