from django import forms


class SearchForm(forms.Form):
    barcode = forms.CharField(max_length=32)