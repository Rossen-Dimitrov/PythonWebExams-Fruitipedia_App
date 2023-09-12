from django.shortcuts import render, redirect

from .forms import ProfileForm


def profile_create(request):
    form = ProfileForm()

    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_page')

    context = {
        "form": form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    return render(request, 'profile/details-profile.html')


def profile_edit(request):
    return render(request, 'profile/edit-profile.html')


def profile_delete(request):
    return render(request, 'profile/delete-profile.html')
