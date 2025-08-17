Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
Configurar o git

git config --global user.name 'Kaio'
git config --global user.email 'projetosyago@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init 
git add .
git commit -m 'Mensagem'
git remote add origin git@github.com:YagoPJ/ProjetoAgendaDjango.gitss