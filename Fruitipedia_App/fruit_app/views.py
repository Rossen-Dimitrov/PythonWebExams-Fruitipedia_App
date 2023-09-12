from django.shortcuts import render, redirect
from Fruitipedia_App.core.profile_utils import get_profile
from Fruitipedia_App.fruit_app.forms import FruitModelForm


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }
    print(profile)
    return render(request, 'index.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def create_fruit(request):
    form = FruitModelForm()
    if request.method == "POST":
        form = FruitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard_page")

    context = {
        'form': form
    }

    return render(request, 'fruit/create-fruit.html', context)


def details_fruit(request, pk):
    return render(request, 'fruit/details-fruit.html')


def edit_fruit(request, pk):
    return render(request, 'fruit/edit-fruit.html')


def delete_fruit(request, pk):
    return render(request, 'fruit/delete-fruit.html')
