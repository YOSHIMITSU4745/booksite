from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):

    def __str__(self):
        return self.name + '-' + self.author
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class profile(models.Model):

    pp = models.ImageField(null=True , blank=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE )
    def __str__(self):
        return self.user.username