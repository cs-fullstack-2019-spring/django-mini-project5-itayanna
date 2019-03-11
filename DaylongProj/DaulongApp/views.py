from django.shortcuts import render, redirect
from .models import NewUserModel, NewRecipeModel
from .forms import RecipeForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, 'DaulongApp/index.html')


@login_required
def homePage(request):
    print('HOME')
    urEntries = NewRecipeModel.objects.filter(creatorOfRecipe=request.user)
    print(urEntries)
    context = {'urEntries': urEntries}
    return render(request, 'DaulongApp/homePage.html', context)


def newUser(request):
    form = UserForm(request.POST or None)
    context = {
        "form": form
    }

    if request.method == 'POST':
        User.objects.create_user(request.POST["username"], "", request.POST["password"])
        form.save()
    return render(request, "DaulongApp/newUser.html", context)


@login_required
def allRecipes(request):
    allEntries = NewRecipeModel.objects.all()
    context = {'allEntries': allEntries}
    return render(request, 'DaulaongApp/allRecipes.html', context)


def newRecipes(request):
    form = RecipeForm(request.POST or None, request.user)
    if form.is_valid() and request.method == "POST":
        # form.save()
        NewRecipeModel.objects.create(picture = request.POST['picture'],
                                      name = request.POST['name'],
                                      description = request.POST['description'],
                                      dateCreated = request.POST['dateCreated'],
                                      creatorOfRecipe= request.user)

        return redirect('homePage')
    return render(request, 'DaulongApp/newRecipes.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'DaulongApp/profile.html')
