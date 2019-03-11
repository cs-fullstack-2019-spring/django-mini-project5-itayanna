from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('homePage/', views.homePage, name='homePage'),
    path('newUser/', views.newUser, name='newUser'),
    path('allRecipes/', views.allRecipes, name='allRecipes'),
    path('newRecipe/', views.newRecipes, name='newRecipes'),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')), ]