from django import forms
from .models import Food, Medicine

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'category', 'quantity', 'units']

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'category', 'owner', 'doses']