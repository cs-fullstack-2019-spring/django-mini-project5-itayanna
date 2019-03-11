from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class NewRecipeModel(models.Model):
    picture = models.CharField(max_length=800, default="")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=6000)
    dateCreated = models.DateField(default= '')
    creatorOfRecipe= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name

class NewUserModel(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, null=True, blank=True)
    confirmPassword = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200)
    profilePic = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
