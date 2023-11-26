from django import forms


class CheckOutForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا نام خود را وارد کنید'
        }
    )

    last_name = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا نام خانوادگی خود را وارد کنید'
        }
    )

    state = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا نام استان خود را وارد کنید'
        }
    )

    city = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا نام شهر خود را وارد کنید'
        }
    )

    phone = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا شماره تلفن خود را وارد کنید'
        }
    )

    zipcode = forms.CharField(
        widget=forms.TextInput(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا کد پستی خود را وارد کنید'
        }
    )

    address = forms.CharField(
        widget=forms.Textarea(),
        label='',
        required=True,
        error_messages={
            'max_length': 'لطفا آدرس را کامل وارد کنید'
        }
    )
