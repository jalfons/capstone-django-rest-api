<<<<<<< HEAD
# portfoliosite
=======
# Little Lemon API

Breve descrizione
- Progetto API REST per un piccolo ristorante: menu, carrello, ordini e gestione gruppi (Managers, Delivery crew).
- Stack: Django REST Framework, SQLite (`db.sqlite3`), venv in `.venv`.

Prerequisiti
- Python 3.10+ (il progetto è testato con Python 3.10). Non forzare aggiornamenti di sistema.

Setup rapido
1. Crea e attiva l'ambiente virtuale nella root del progetto:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Installa dipendenze:

```bash
pip install -r requirements.txt
```

3. Applica migrazioni e crea superuser (facoltativo):

```bash
python manage.py migrate
python manage.py createsuperuser
```

Esecuzione

```bash
python manage.py runserver 0.0.0.0:8000
```

Autenticazione
- L'API usa Token Auth (`rest_framework.authtoken`). Dopo aver creato un utente admin è possibile generare un token dall'admin o usare il file `token.txt` se presente.
- Esempio header:

```bash
curl -H "Authorization: Token <YOUR_TOKEN>" http://127.0.0.1:8000/api/orders
```

Endpoint principali
- `GET/POST /api/menu-items` — lista e creazione (creazione: admin/managers).
- `GET/POST /api/categories` — gestione categorie (create: admin).
- `GET/POST /api/cart/menu-items` — aggiungi/rimuovi elementi nel carrello (autenticato).
- `GET/POST /api/order` e alias `GET/POST /api/orders` e `GET/PUT/PATCH/DELETE /api/orders/<id>` — ordini (filtrati per ruolo).
- Group management: `/api/groups/managers/users` e `/api/groups/delivery-crew/users` (aggiungi/rimuovi utenti).

Compatibilità retroattiva
- Sono presenti alias per compatibilità con client legacy: `/api/categories`, `/api/cart/orders` (→ `OrderView`), `/api/orders` e `/api/order`, e altre forme plurale/singolare per i group routes.

Permessi e comportamento ordini
- `OrderView` filtra gli ordini in base al ruolo:
  - superuser / Managers → tutti gli ordini
  - Delivery crew → ordini assegnati a loro
  - utenti normali → solo i propri ordini
- `SingleOrderView` restituisce gli items dell'ordine; permette toggle status e assegnazione di `delivery_crew`.

Fix recenti e note tecniche
- Django è stato pinned a `5.x` per compatibilità con Python 3.10 (modifica in `requirements.txt`).
- Correzioni applicate:
  - uso corretto di `request.user.groups` (non `user.group`), check case-insensitive su gruppi (`groups__name__iexact`).
  - rimosso lookup errato `groups_name` e corretto in `models.py` e in migration `0005`.
  - aggiunte rotte alias per compatibilità (es. `cart/orders`).

Esempi rapidi

Lista ordini (autenticato):
```bash
curl -H "Authorization: Token <YOUR_TOKEN>" http://127.0.0.1:8000/api/orders
```

Vedere gli item di un ordine:
```bash
curl -H "Authorization: Token <YOUR_TOKEN>" http://127.0.0.1:8000/api/orders/1
```

Contribuire / prossimi passi
- Aggiungere fixtures/seed per dati di esempio.
- Aggiungere test automatizzati e CI (GitHub Actions).

File utili
- `manage.py`, `requirements.txt`, `db.sqlite3`, `token.txt` (token di test, se presente).

Licenza
- Aggiungi qui la licenza che preferisci prima di pubblicare su GitHub.

---
README generato automaticamente — posso adattarlo (più dettagli, badge, esempi curl estesi) se vuoi.

Littlelemon Django API

Run locally (from project root):

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip setuptools wheel
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Important notes:
- This repo was pinned to `Django>=5.2,<6` for local Python 3.10 compatibility.
- Admin user `admin` exists; `devadmin` was created; token for `devadmin` was generated in this session.
- Example API endpoints:
  - GET /api/menu-items  (lists menu items)
  - GET /api/menu-items/<id>
  - POST/GET /api/cart/menu-items (requires token auth)

To generate a token for a user:

```bash
python manage.py drf_create_token <username>
```
>>>>>>> fbed36f (Clean project structure)
