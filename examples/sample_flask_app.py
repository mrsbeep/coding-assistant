# Sample Python Flask Web App
# This file contains intentional issues for demonstration purposes

from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Security issue: Secret key should not be hardcoded
app.secret_key = "hardcoded_secret_key"

# Database connection function without proper error handling
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# API endpoint with SQL injection vulnerability
@app.route('/users/<user_id>')
def get_user(user_id):
    conn = get_db_connection()
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = conn.execute(query).fetchall()
    conn.close()
    return jsonify(result)

# Missing input validation
@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json['username']  # No error handling for missing key
    email = request.json['email']        # No validation
    
    conn = get_db_connection()
    conn.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                (username, email))
    conn.commit()
    conn.close()
    return jsonify({"message": "User created"})

# Inefficient database query in loop
@app.route('/user_stats')
def get_user_stats():
    conn = get_db_connection()
    users = conn.execute("SELECT id FROM users").fetchall()
    
    stats = []
    for user in users:
        # N+1 query problem
        user_data = conn.execute("SELECT * FROM user_activity WHERE user_id = ?", 
                                (user[0],)).fetchall()
        stats.append({"user_id": user[0], "activity_count": len(user_data)})
    
    conn.close()
    return jsonify(stats)

if __name__ == '__main__':
    # Debug mode should not be enabled in production
    app.run(debug=True, host='0.0.0.0')  # Security risk: binding to all interfaces