# 🎵 Music Backend (Django + GraphQL)

Backend for the **Music App** project.
This service provides a **GraphQL API** for managing **Artists, Albums, and Songs** and is designed to be consumed by a separate React frontend.

---

## 🚀 Tech Stack

- **Python**
- **Django**
- **Graphene-Django** (GraphQL integration)
- **SQLite** (development database)

---

## 🧠 Architecture Note

This project was **initially scaffolded using REST APIs** to better understand Django fundamentals 
(models, serializers, views, and routing).

After establishing a solid foundation, the backend was **refactored to use GraphQL (Graphene-Django)** 
as the primary API layer, providing a more flexible, efficient, and scalable data-fetching approach 
better suited for modern frontend applications.

---

## 📂 Project Structure

- `backend/` — Django project (settings, urls, wsgi, asgi)
- `music/` — Django app (models, serializers, views, urls)
- `manage.py` — Django management script
- `requirements.txt` — Python dependencies
- `.env.example` — Environment variables template

---

## ⚙️ Setup (Local Development)

Follow these steps to run the project locally.

1. Clone the repository

```bash
git clone https://github.com/itskhashman/Music-backend.git
cd Music-backend
```

2. Create a virtual environment

```bash
python -m venv .venv
```

3. Activate the virtual environment

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Environment variables

Create a `.env` file in the project root (same level as `manage.py`) and copy values from `.env.example`.

Example `.env.example`:

```env
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

6. Run database migrations

```bash
python manage.py migrate
```

7. Start the development server

```bash
python manage.py runserver
```

The GraphQL endpoint will be available at:

http://127.0.0.1:8000/graphql/ or http://localhost:8000/graphql/ 

---
