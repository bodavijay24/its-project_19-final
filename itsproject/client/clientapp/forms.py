from django import forms

class HomeForm(forms.Form):
	Aadhar=forms.IntegerField(label="Your Aadhar")
	passwd=forms.CharField(label="Passwrd")
	
class DealForm(forms.Form):
	Aadhar=forms.IntegerField(label="Your Aadhar")
	passwd=forms.CharField(label="Passwrd")
	
class VillForm(forms.Form):
	Village=forms.CharField(label="village name")
