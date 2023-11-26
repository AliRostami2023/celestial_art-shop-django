from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'نام محصول را وارد کنید',
            'class': 'form-control'
        }),
        label='',
        required=False
    )
