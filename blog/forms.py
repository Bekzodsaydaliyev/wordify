from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            "id": "message",
            "class": "form-control",
            "name": "message",
            "cols": 30,
            "rows": 8,
        })