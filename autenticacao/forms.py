from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    pass


class CriarUsuarioForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Senha (mín. 8 caracteres)',
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'O usuário "{username}" já existe.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres.')
        return password
