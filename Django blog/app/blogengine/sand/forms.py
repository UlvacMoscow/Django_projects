from django import forms



class VampireCreateForm(forms.Form):
    name = forms.CharField()
    damage = forms.IntegerField()
    health = forms.IntegerField()
    groups = forms.Membership()
