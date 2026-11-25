from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """Formulário de login com o visual do site."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Usuário'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite seu usuário',
            'autocomplete': 'username',
        })

        self.fields['password'].label = 'Senha'
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite sua senha',
            'autocomplete': 'current-password',
        })


class CadastroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seuemail@exemplo.com',
            'autocomplete': 'email',
        }),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Usuário'
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Escolha seu usuário',
            'autocomplete': 'username',
        })

        self.fields['password1'].label = 'Senha'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Crie uma senha',
            'autocomplete': 'new-password',
        })

        self.fields['password2'].label = 'Confirmar senha'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Digite a senha novamente',
            'autocomplete': 'new-password',
        })
