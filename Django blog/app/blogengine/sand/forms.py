from django import forms



class VampireCreateForm(forms.Form):
    name = forms.CharField()
    damage = forms.IntegerField()
    # groups = forms.Man
