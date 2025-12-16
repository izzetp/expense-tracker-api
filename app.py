# app.py

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect("expenses.db")
    conn.row_factory = sqlite3.Row
    return conn

# GET expenses
@app.route("/expenses", methods=["GET"])
def get_expenses():
    conn = get_db_connection()
    expenses = conn.execute("SELECT * FROM expenses").fetchall()
    conn.close()
    return jsonify([dict(row) for row in expenses])

# Post expenses
@app.route("/expenses", methods=["POST"])
def add_expenses():
    data = request.get_json()
    if not data:
        return {"error":"Invalid JSON"}
    category_ = data.get("category"), 400
    amount = data.get("amount")
    date = data.get("date")

    if not all ([category_, amount, date]):
        return {"error": "Missing fields"}, 400
    
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)" , (category_, amount, date)
    )
    conn.commit()
    conn.close()

    return {"message": "Expense added", "expense": data}, 201

if __name__ == '__main__':
    app.run(debug=True)