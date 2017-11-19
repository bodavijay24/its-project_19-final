from django import forms
class HomeForm(forms.Form):
    Hid = forms.IntegerField()
    Name=forms.CharField()
    Age=forms.IntegerField()
    Gender=forms.CharField()
