from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import re

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            name TEXT NOT NULL,
            recovery_code TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        if user:
            return redirect(url_for('menu'))
        else:
            return "Неверный email или пароль"

    return render_template('log.html')

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        name = request.form['name']
        recovery_code = request.form['recovery_code']

        if password != repeat_password:
            return "Пароли не совпадают!"

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            return "Пользователь с таким email уже существует!"

        cursor.execute("INSERT INTO users (email, password, name, recovery_code) VALUES (?, ?, ?, ?)",
                       (email, password, name, recovery_code))
        conn.commit()
        conn.close()

        return redirect(url_for('menu'))

    return render_template('reg.html')

@app.route('/forgot_pass', methods=['GET', 'POST'])
def forgot_pass():
    if request.method == 'POST':
        email = request.form['email'].strip()
        recovery_code = request.form['recovery_code'].strip()

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ? AND recovery_code = ?", (email, recovery_code))
        user = cursor.fetchone()

        if user:
            return redirect(url_for('reset_pass', user_id=user['id']))
        else:
            return "Неверный email или код восстановления"

    return render_template('forgot_pass.html')

@app.route('/reset_pass/<int:user_id>', methods=['GET', 'POST'])
def reset_pass(user_id):
    if request.method == 'POST':
        new_password = request.form['new_password']
        repeat_password = request.form['repeat_password']

        if new_password != repeat_password:
            return "Пароли не совпадают!"

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (new_password, user_id))
        conn.commit()
        conn.close()

        return redirect(url_for('log'))

    return render_template('reset_pass.html')

if __name__ == '__main__':
    app.run(debug=True)
