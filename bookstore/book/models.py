from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class Book(models.Model):
    title=models.CharField(max_length=50)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    published_date=models.DateTimeField(auto_now_add=True)
    isbn=models.CharField(max_length=20, unique=True)
    price=models.BooleanField()
    stock=models.IntegerField()

    def __str__(self):
        return self.title
    
class Country(models.Model):
    name=models.CharField(max_length=50, unique=True)
    code=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name