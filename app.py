import json
import os

from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request, url_for
from pymongo import MongoClient

# Load variables from a local .env file (ignored by git)
load_dotenv()

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Secrets come from the environment, never from the source code
MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("DB_NAME", "flask_assignment_db")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "submissions")

collection = None
if not MONGO_URI:
    print("WARNING: MONGO_URI is not set. Copy .env.example to .env and fill it in.")
else:
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        collection = client[DB_NAME][COLLECTION_NAME]
    except Exception as e:
        print("Failed to create MongoDB client:", e)


# Task 2: Frontend form route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if not name or not email:
            return render_template("index.html", error="All fields are required!")

        if collection is None:
            return render_template(
                "index.html", error="Database is not configured. Set MONGO_URI."
            )

        try:
            collection.insert_one({"name": name, "email": email})
            return redirect(url_for("success"))
        except Exception as e:
            # Show the error on the same page, no redirect
            return render_template("index.html", error=f"Database error: {e}")

    return render_template("index.html", error=None)


@app.route("/success")
def success():
    return render_template("success.html")


# Task 1: JSON API route
@app.route("/api", methods=["GET"])
def api_route():
    try:
        with open(os.path.join(BASE_DIR, "data.json"), "r") as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify([{"error": "Failed to read data file", "details": str(e)}]), 500


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG", "0") == "1")
