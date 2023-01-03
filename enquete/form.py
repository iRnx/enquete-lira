from django import forms
from .models import Resposta

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['resposta_pergunta'].widget.attrs['class'] = 'form-control'
        self.fields['resposta_pergunta'].widget.attrs['placeholder'] = 'Resposta da pergunta'

    # def clean_resposta_pergunta(self):
    #     resposta_pergunta = self.cleaned_data.get('resposta_pergunta')

    #     if any(char.isdigit() for char in resposta_pergunta):
    #         self.add_error('resposta_pergunta', 'Campo nome n pode conter números.')
    #     else:
    #         return resposta_pergunta