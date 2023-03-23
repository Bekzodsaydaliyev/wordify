from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].widget.attrs.update({
            "name": "message",
            "id": "message",
            "class": "form-control",
            "rows": 5,
            "cols": 30,
            "placeholder": "message",
        })
        self.fields['email'].widget.attrs.update({
            "type": "text",
            "class": "form-control",
            "placeholder": "email",
        })
        self.fields['name'].widget.attrs.update({
            "type": "text",
            "id": "name",
            "class": "form-control",
            "placeholder": "name",
        })
        self.fields['subject'].widget.attrs.update({
            "type": "text",
            "placeholder": "subject",
            "class": "form-control",
        })