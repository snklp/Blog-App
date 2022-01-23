from importlib.resources import contents
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# WHAT WE WANNA SAVE INN THE DATABASE
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # USER(SEPERATE TABLE) IS AUTHOR CREARING THE POST

    # POST MODEL AND USER MODEL IS GONNA HAVE A RELATIONSHIP SINCE USERS ARE GOING TO AUTHOR POSTS (one -> many)

    def __str__(self):
        return self.title

