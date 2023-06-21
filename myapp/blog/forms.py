from django import forms
from .models import Post


# Form : html에 있는 form tag
# Model Form : model을 사용하는 form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]
