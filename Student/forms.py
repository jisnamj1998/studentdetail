from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control btn btn-outline-primary"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control btn btn-outline-primary"}))
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control btn btn-outline-primary"}))
    score=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control btn btn-outline-primary"}))
    division=forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control btn btn-outline-primary"}))