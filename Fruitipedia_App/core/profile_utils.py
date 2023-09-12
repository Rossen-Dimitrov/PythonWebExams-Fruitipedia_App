from Fruitipedia_App.profile_app.models import ProfileModel


def get_profile():
    return ProfileModel.objects.first()
