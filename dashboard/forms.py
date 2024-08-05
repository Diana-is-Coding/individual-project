from django import forms
from .models import Goods, List

class GoodsForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', 'category', 'owner', 'quantity', 'units']

class ListForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Goods.objects.all())