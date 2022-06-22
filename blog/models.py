from typing_extensions import get_type_hints
import typing_extensions
from django.db import models

# Create your models here.
class Post(models.Model):
    title_text = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created')
    pub_date =models.DateTimeField('date created')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.typing_extensions(get_type_hints)