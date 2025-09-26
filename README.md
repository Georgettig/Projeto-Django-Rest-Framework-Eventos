# 🎯 Projeto API com Django Rest Framework

Este projeto é uma aplicação de **API RESTful** desenvolvida com **Django Rest Framework (DRF)**.  
A API gerencia **Eventos**, **Participantes** e **Inscrições**, permitindo cadastrar, consultar, atualizar e remover registros.  

🎯 Objetivo
- Este projeto foi desenvolvido com fins de aprendizado em Django Rest Framework, praticando a criação de APIs RESTful com relacionamentos entre modelos.

🚀 Tecnologias utilizadas
- Python 3.x
- Django
- Django Rest Framework
- SQLite (banco de dados padrão)


⚙️ Como rodar o projeto localmente

### 1. Clone o repositório
```bash
git clone https://github.com/Georgettig/Projeto-Django-Rest-Framework-Eventos.git
cd Projeto-Django-Rest-Framework-Eventos
python -m venv .venv
.venv.\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

