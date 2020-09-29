from django import forms

from . import models


class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = 'body',
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Содержание поста'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['body'].label = False
