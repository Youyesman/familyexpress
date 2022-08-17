from django import forms

class Userform(forms.Form):
    username        = forms.CharField(max_length=254) #아이디
    password = forms.CharField(max_length=254)
    confirm = forms.CharField(max_length=254)
    name = forms.CharField(max_length=10) #이름
    team = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=20)
