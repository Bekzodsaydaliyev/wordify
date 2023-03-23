from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.CharField(max_length=222)
    message = models.TextField()

    def __str__(self):
        return self.name

