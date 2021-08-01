from django import forms

class StudentForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)