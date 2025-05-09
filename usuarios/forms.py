from django import forms
from app_1.models import Fotografia
class LoginForms(forms.Form):
    email_login = forms.EmailField(
        label = "Digite seu email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    senha = forms.CharField(
        label = "Digite sua senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
   
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Digite seu nome e sobrenome",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control"
            }
        )
        
    )

    email = forms.EmailField(
        label = "Digite seu email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    criar_senha = forms.CharField(
        label = "Digite a senha que desejar usar",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    confirmar_senha = forms.CharField(
        label = "Confirme sua senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control"
            }
        )
    )
    def clean_confirmar_senha(self):
        senha_1 = self.cleaned_data.get("criar_senha")
        senha_2 = self.cleaned_data.get("confirmar_senha")
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Por favor, digite senhas iguais!")
            else:
                return senha_2
                
    def clean_nome_cadastro(self):
        nome_sobrenome = self.cleaned_data.get("nome_cadastro")
        for caractere in nome_sobrenome:
            if caractere.isdigit():
                raise forms.ValidationError("Digite apenas letras!")
        partes_nome = nome_sobrenome.split()
        
        if len(partes_nome) != 2:
            raise forms.ValidationError("Por favor, insira nome e sobrenome!")
        
        return nome_sobrenome
        
    def pegar_sobrenome(self):
        nome_sobrenome = self.cleaned_data.get("nome_cadastro")
        partes_nome = nome_sobrenome.split()
        primeiro_nome = partes_nome[0]
        sobrenome = partes_nome[1]
        return primeiro_nome, sobrenome
    
class UploadForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        fields = ["nome", "legenda", "descricao", "categoria", "foto", "publicado"]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a legenda'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

