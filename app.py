from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# ✅ Database connection
db = mysql.connector.connect(
    host="localhost",
    user="digital_user",
    password="your_password",
    database="digital_dining",
    port=3306
)

# ✅ Create a cursor
cursor = db.cursor(dictionary=True)

# ---------- ROUTES ----------

@app.route("/")
def home():
    return "Welcome to Digital Dining Backend!"

@app.route("/menu")
def get_menu():
    cursor.execute("SELECT * FROM menu_items")
    menu = cursor.fetchall()
    return jsonify(menu)

@app.route("/users")
def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
