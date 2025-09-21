from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# ✅ Database connection
try:
    db = mysql.connector.connect(
        host="localhost",
        user="digital_user",
        password="your_password",
        database="digital_dining",
        port=3306
    )
    cursor = db.cursor(dictionary=True)
    print("✅ Database connected successfully")
except Error as e:
    print(f"❌ Error connecting to database: {e}")
    db = None
    cursor = None

# ---------- ROUTES ----------

@app.route("/")
def home():
    return "Welcome to Digital Dining Backend!"

@app.route("/menu")
def get_menu():
    if not cursor:
        return jsonify({"error": "Database connection not established"}), 500
    try:
        cursor.execute("SELECT * FROM menu_items")
        menu = cursor.fetchall()
        return jsonify(menu)
    except Error as e:
        return jsonify({"error": str(e)}), 500

@app.route("/users")
def get_users():
    if not cursor:
        return jsonify({"error": "Database connection not established"}), 500
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users)
    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
