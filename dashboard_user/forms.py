from django import forms
from django.core.exceptions import ValidationError


class ChangePasswordUserForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='کلمه عبور فعلی'
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='کلمه عبور جدید'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار کلمه عبور جدید'
    )

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if new_password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور جدید و تکرار آن یکسان نیستند...')

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')

        if len(new_password) >= 8:
            return new_password

        raise ValidationError('کلمه عبور باید حداقل شامل 8 رقم یا کاراکتر باشد')
