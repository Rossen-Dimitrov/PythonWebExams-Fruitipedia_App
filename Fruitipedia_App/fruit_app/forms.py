from django import forms

from Fruitipedia_App.fruit_app.models import FruitModel


class FruitModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = ('name', 'image_url', 'description', 'nutrition')
        labels = {
            "name": "",
            "image_url": "",
            "description": "",
            "nutrition": "",
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.TextInput(attrs={'placeholder': 'Fruit image URL'}),
            'description': forms.TextInput(attrs={'placeholder': 'Fruit description'}),
            'nutrition': forms.TextInput(attrs={'placeholder': 'Nutrition Info'}),
        }