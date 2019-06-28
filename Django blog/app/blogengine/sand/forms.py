from django import forms
from .models import Vampire


class VampireCreateForm(forms.Form):
    class Meta:
        model = Vampire
        fields = ['name', 'damage', 'health', 'groups']
    # name = forms.CharField()
    # damage = forms.IntegerField()
    # health = forms.IntegerField()
    # groups = forms.Membership()
