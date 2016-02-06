from django import forms


class SearchForm(forms.Form):
    email = forms.EmailField(max_length=50)


class XpForm(forms.Form):
    xp = forms.CharField(min_length=1, max_length=50,  widget=forms.TextInput(attrs={'placeholder': 'Enter the amount of xp for user', 'autofocus':'autofocus'}))
