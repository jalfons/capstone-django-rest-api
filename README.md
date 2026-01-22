Little Lemon API (Capstone)

REST API per la gestione di menu, carrello e ordini, con autenticazione e permessi differenziati per ruolo.
Capstone project del percorso Meta Full-Stack Developer (Coursera).

Il progetto implementa:
- autenticazione Token
- ruoli (Admin, Manager, Delivery Crew, Customer)
- gestione menu, categorie, carrello e ordini
- filtri sugli ordini in base al ruolo
- paginazione, ordinamento e ricerca

Stack utilizzato:
- Python 3.10
- Django
- Django REST Framework
- SQLite (sviluppo/testing locale)

Setup locale:

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Server locale disponibile su:
http://127.0.0.1:8000/

Autenticazione:

L’API utilizza Token Authentication (rest_framework.authtoken).

Header richiesto per le richieste protette:
Authorization: Token <YOUR_TOKEN>

Login utente:
POST /auth/token/login/

Registrazione utente:
POST /auth/users/
