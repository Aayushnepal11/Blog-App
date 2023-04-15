from django.db import models
from uuid import uuid4
from ckeditor.fields import RichTextField
from django.urls import reverse
from users.models import User

class BlogPost(models.Model):
    id = models.IntegerField(editable=False, primary_key=True, default=uuid4)
    title = models.CharField(max_length=150)
    text = RichTextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Blog Post")
        verbose_name_plural = ("Blog Posts")

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("blogs:home")
    