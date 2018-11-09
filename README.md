**Requerimentos**

*Git*

*Python 3 +*

---

**Primeiro passo:**
*Download do projeto*

Use o comando cd localdesejado para entrar pasta na qual você deseja baixar o projeto.

Use o comando `git clone https://github.com/Mendelski/CrudDjango` para baixar o projeto. 

Link do GitHub [CrudDjango](https://github.com/Mendelski/CrudDjango)

---
**Segundo passo:**
*Criação do venv e instalação do Django*.

Use o comando: `python -m venv myVenv` para criar uma myVenv.

*(Talvez o comando python não seja reconhecido, caso isso aconteça use py)*.

Use o comando `cd myVenv/Scripts` e após isso use `activate` para inicializar o seu venv.

Use o comando `pip install Django==2.0.7` para instalar o Django em sua venv.

---
**Terceiro passo:**
*Rodando*

Use o comando cd ../../ e cd CrudDjango para entrar na pasta do projeto

Use o comando python manage.py makemigrations e python manage.py migrate para criar o banco de dados

Use o comando python manage.py runserver para rodar o servidor local e entre em localhost:8000 em seu browser para abrir o sistema

---