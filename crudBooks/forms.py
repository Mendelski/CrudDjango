from django.forms import ModelForm
from .models import Livro

class LivroForm(ModelForm):
	class Meta:
		model = Livro
		fields = ['nome', 'autor', 'edicao']


	def __init__(self, *args, **kwargs):
		super(LivroForm, self).__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs['class'] = 'form-control'
		self.fields['autor'].widget.attrs['class'] = 'form-control'
		self.fields['edicao'].widget.attrs['class'] = 'form-control'