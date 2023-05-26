from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.CharField(max_length=100)
    published_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=50)


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)

