from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CadastroForm(UserCreationForm):
    email = forms.EmailField(
    required=True,
    label='E-mail',
    widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'placeholder': '[seuemail@exemplo.com](mailto:seuemail@exemplo.com)',
    'autocomplete': 'email',
})
)

class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

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

