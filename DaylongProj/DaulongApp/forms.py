from django import forms
from .models import NewRecipeModel, NewUserModel


class RecipeForm(forms.ModelForm):
    class Meta:
        exclude = ['creatorOfRecipe']
        model = NewRecipeModel


class UserForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = NewUserModel
