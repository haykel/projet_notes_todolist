# 📝 Todo & Notes API

API REST développée avec **Django** et **Django REST Framework** permettant de gérer des **todos (tâches)** et des **notes**, avec une relation entre les deux.

Le projet est entièrement exposé via une API REST, sécurisée par **JWT**, et documentée avec **Swagger (OpenAPI)**.

---

## 🚀 Stack technique

- Python 3.12
- Django 5
- Django REST Framework
- JWT (SimpleJWT)
- Swagger / OpenAPI (drf-spectacular)
- Pytest (tests API)
- SQLite (par défaut)

---

## 🧱 Architecture du projet

```text
projet_notes_todolist/
├── config/              # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/               # App Todos
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── tests/
├── notes/               # App Notes
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── tests/
├── manage.py
├── requirements.txt
└── README.md

---

## 🔗 Modélisation

### Todo
- `title` (string)
- `status` (todo / done)
- `note` (optionnelle)

### Note
- `title`
- `content`
- peut être liée à plusieurs todos

### Relations
- Une **todo** peut référencer **une note**
- Une **note** peut avoir **plusieurs todos**
- Les todos peuvent exister sans note

---

## 🧠 Choix métier importants

### Suppression d’une note
- La suppression d’une note **ne supprime pas les todos**
- Les todos restent en base mais leur `note_id` devient `null`
- Les todos sans note sont **cachées côté API**

Ce choix permet d’éviter la perte de données tout en conservant une API cohérente.

---

## 🔐 Authentification (JWT)

L’API est sécurisée globalement par JWT.

### Endpoints d’authentification
- `POST /api/token/` → obtenir un access token et un refresh token
- `POST /api/token/refresh/` → rafraîchir l’access token

Toutes les APIs métiers sont protégées par défaut.

---

## 📚 Documentation API (Swagger)

La documentation Swagger est accessible à l’adresse :

http://localhost:8000/api/docs/


### Utilisation
1. Appeler `/api/token/`
2. Copier le champ `access`
3. Cliquer sur **Authorize**
4. Entrer :
Bearer <access_token>

---

## 🔍 Endpoints principaux

### Todos
- `GET /api/todos/`
- `POST /api/todos/`
- `GET /api/todos/{id}/`
- `PATCH /api/todos/{id}/`
- `DELETE /api/todos/{id}/`

### Notes
- `GET /api/notes/`
- `POST /api/notes/`
- `GET /api/notes/{id}/`
- `PATCH /api/notes/{id}/`
- `DELETE /api/notes/{id}/`

---

## 🧪 Tests

Les tests couvrent :
- CRUD des Todos
- CRUD des Notes
- Relations Notes ↔ Todos
- Sécurité (JWT)

Lancer les tests :
pytest

---
## ⚙️ Installation et lancement

# Cloner le projet
git clone https://github.com/haykel/projet_notes_todolist.git
cd projet_notes_todolist

# Créer l’environnement virtuel
python3.12 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver

