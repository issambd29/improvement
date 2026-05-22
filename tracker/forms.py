from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

INPUT_ATTRS = {
    'style': (
        'width:100%; background:#0d1f12; border:1px solid #182c1c; border-radius:10px;'
        'padding:0.75rem 1rem; color:#d8edd9; font-size:0.9rem; font-family:Inter,sans-serif;'
        'outline:none; direction:ltr;'
    )
}


class StyledUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={**INPUT_ATTRS, 'placeholder': 'username', 'autocomplete': 'username'}),
        label='اسم المستخدم / Username',
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={**INPUT_ATTRS, 'placeholder': '••••••••', 'autocomplete': 'new-password'}),
        label='كلمة المرور / Password',
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={**INPUT_ATTRS, 'placeholder': '••••••••', 'autocomplete': 'new-password'}),
        label='تأكيد كلمة المرور / Confirm Password',
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
