from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def home(request):
	data = {}
	data['livros'] = Livro.objects.all()
	return render(request, 'crudBooks/index.html', data)


def create(request):
	form = LivroForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'crudBooks/new.html', {'livroForm':form})


def update(request, pk):
	livro = Livro.objects.get(pk=pk)
	form = LivroForm(request.POST or None, instance=livro)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'crudBooks/update.html', {'livroForm':form})

def delete(request, pk):
    livro=Livro.objects.get(pk=pk)
    livro.delete()
    return redirect('home')