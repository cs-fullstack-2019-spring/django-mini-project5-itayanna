from django.contrib import admin
from .models import NewRecipeModel, NewUserModel
# Register your models here.
admin.site.register(NewRecipeModel)
admin.site.register(NewUserModel)