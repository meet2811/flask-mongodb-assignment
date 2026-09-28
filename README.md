# Flask and MongoDB Atlas Assignment

A small Flask app with two parts:

- **Task 1 – JSON API:** `GET /api` reads `data.json` and returns it as JSON.
- **Task 2 – Form + MongoDB Atlas:** `GET/POST /` shows a form (name, email) and saves it to MongoDB Atlas. On success it redirects to `/success`; on error it shows the message on the same page.

## Project structure

```
.
├── app.py
├── data.json
├── requirements.txt
├── .env.example
├── .gitignore
└── templates/
    ├── index.html
    └── success.html
```

## Prerequisites

- Python 3.9+
- A free MongoDB Atlas cluster (https://www.mongodb.com/cloud/atlas)

## Setup

1. Clone the repo and enter the folder:
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd <repo-folder>
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   ```bash
   # Windows
   copy .env.example .env
   # macOS / Linux
   cp .env.example .env
   ```
   Open `.env` and set `MONGO_URI` to your Atlas connection string.

### Getting the Atlas connection string

1. Atlas dashboard → **Database Access** → create a database user (username + password).
2. **Network Access** → add your IP address (or `0.0.0.0/0` for testing only).
3. **Database** → **Connect** → **Drivers** → copy the `mongodb+srv://...` string.
4. Replace `<password>` with your user's password. If the password has special characters, URL-encode them.

## Run

```bash
python app.py
```

Open http://127.0.0.1:5000

## Endpoints

| Route      | Method    | Description                                  |
|------------|-----------|----------------------------------------------|
| `/`        | GET, POST | Form; saves name and email to Atlas          |
| `/success` | GET       | Shown after a successful submission          |
| `/api`     | GET       | Returns the contents of `data.json` as JSON  |

## Security notes

- The MongoDB connection string is read from the `MONGO_URI` environment variable.
- `.env` is listed in `.gitignore` and is never committed. Only `.env.example` (placeholders) is.
