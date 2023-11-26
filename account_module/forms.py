from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        label='نام'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }),
        label='نام خانوادگی'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='کلمه عبور'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='تکرار کلمه عبور'
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) >= 8:
            return password

        raise ValidationError('کلمه عبور باید حداقل شامل 8 رقم یا کاراکتر باشد')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار ان با هم مغایرت ندارند')


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }),
        label='ایمیل'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='کلمه عبور'
    )


class ForgetPassForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }),
        label='ایمیل'
    )


class ResetPassForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='کلمه عبور جدید'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='تکرار کلمه عبور'
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار ان با هم مغایرت ندارند')

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) >= 8:
            return password

        raise ValidationError('کلمه عبور باید حداقل شامل 8 رقم یا کاراکتر باشد')
