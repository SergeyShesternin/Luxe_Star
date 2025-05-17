from flask import Flask, render_template_string, request, redirect, url_for
import re
import sqlite3

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
def main():
    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Luxe Star — Главная</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background: linear-gradient(to right, #e0eafc, #cfdef3);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                position: relative;
            }

            .login-container {
                position: absolute;
                top: 20px;
                right: 20px;
            }

            .login-btn {
                background-color: #28a745;
                color: white;
                padding: 12px 20px;
                border: none;
                border-radius: 6px;
                font-size: 16px;
                cursor: pointer;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }

            .login-btn:hover {
                background-color: #1e7e34;
            }

            .container {
                max-width: 600px;
                width: 90%;
                background-color: #ffffff;
                padding: 60px 30px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
                text-align: center;
            }

            h1 {
                font-size: 36px;
                margin-bottom: 20px;
                color: #333;
            }

            p {
                font-size: 18px;
                color: #555;
                margin-bottom: 30px;
            }

            .btn {
                display: inline-block;
                width: 220px;
                padding: 12px;
                margin: 10px 5px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
                font-size: 16px;
                text-decoration: none;
                transition: background-color 0.3s ease;
            }

            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="login-container">
            <form action="/log">
                <button class="login-btn">Войти в аккаунт и перейти к меню</button>
            </form>
        </div>
        <div class="container">
            <h1>Luxe Star</h1>
            <p>Добро пожаловать в Luxe Star — место, где комфорт, стиль и качество объединяются для вашего идеального отдыха.</p>
            <a href="/about" class="btn">Узнать больше</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route('/about')
def about():
    about_content = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>О нас — Luxe Star</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 40px;
                background-color: #f8f9fa;
                color: #333;
            }
            .content {
                max-width: 800px;
                margin: auto;
                background-color: #ffffff;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                text-align: center;
                margin-bottom: 20px;
            }
            p {
                line-height: 1.6;
                font-size: 18px;
            }
            a {
                display: block;
                text-align: center;
                margin-top: 30px;
                color: #007BFF;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="content">
            <h1>О нас</h1>
            <p><strong>Luxe Star</strong> — это не просто заведение, это атмосфера уюта, элегантности и безупречного сервиса. 
            Мы стремимся создать для наших гостей пространство, где каждый сможет почувствовать себя особенным.</p>
            <p>Наша команда состоит из профессионалов, которые любят своё дело и делают всё возможное, чтобы ваш визит стал по-настоящему приятным и запоминающимся.</p>
            <a href="/">← Вернуться на главную</a>
        </div>
    </body>
    </html>
    '''
    return render_template_string(about_content)


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

    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <title>Регистрация в аккаунт</title>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f2f2f2;
          }
          .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          }
          h3 {
            margin: 10px 0;
          }
          input {
            width: 200px;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
          }
          a {
            display: block;
            margin-bottom: 10px;
            color: #000000;
            text-decoration: none;
          }
          button {
            width: 220px;
            padding: 10px;
            margin: 20px auto;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
          }
          button:hover {
            background-color: #0056b3;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Регистрация</h2>
          <form method="POST">
            <a>Введите почту</a>
            <input type="text" name="email" placeholder="Введите почту">
            <a>Введите пароль</a>
            <input type="password" name="password" placeholder="Введите пароль">
            <a>Повторите пароль</a>
            <input type="password" name="repeat_password" placeholder="Повторите пароль">
            <a>Ваше имя</a>
            <input type="text" name="name" placeholder="Ваше имя">
            <a>6-ти значный код восстановления</a>
            <input type="text" name="recovery_code" placeholder="Введите код восстановления">
            <a>Зарегистрироваться</a>
            <button type="submit">Зарегистрироваться</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


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

    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Забыли пароль</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f2f2f2;
            }
            .container {
                text-align: center;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }
            input {
                width: 200px;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                width: 220px;
                padding: 10px;
                margin: 20px auto;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Восстановить пароль</h2>
            <form method="POST">
                <input type="text" name="email" placeholder="Введите email" required><br>
                <input type="text" name="recovery_code" placeholder="Код восстановления" required><br>
                <button type="submit">Восстановить пароль</button>
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html_content)


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

    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <title>Восстановление пароля</title>
        <style>
          body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f2f2f2;
              }
              .container {
                text-align: center;
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
              }
              h3 {
                margin: 10px 0;
              }
              input {
                width: 200px;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
              }
              a {
                display: block;
                margin-bottom: 10px;
                color: #000000;
                text-decoration: none;
              }
              button {
                width: 220px;
                padding: 10px;
                margin: 20px auto;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
              }
              button:hover {
                background-color: #0056b3;
              }
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Восстановление пароля</h2>
          <a>Введите новый пароль</a>
          <form method="POST">
            <input type="password" name="new_password" placeholder="Введите пароль">
            <a>Повторите новый пароль</a>
            <input type="password" name="repeat_password" placeholder="Повторите пароль">
            <a>Восстановить пароль</a>
            <button type="submit">Восстановить пароль</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


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

    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <title>Вход в аккаунт</title>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f2f2f2;
          }
          .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          }
          h3 {
            margin: 10px 0;
          }
          input {
            width: 200px;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
          }
          a {
            display: block;
            margin-bottom: 10px;
            color: #000000;
            text-decoration: none;
          }
          button {
            width: 220px;
            padding: 10px;
            margin: 20px auto;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
          }
          button:hover {
            background-color: #0056b3;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Вход</h2>
          <form method="POST">
            <a>Войдите в аккаунт или</a>
            <a style="color: #0000FF" href="/reg">зарегистрируйтесь</a>
            <a>Введите почту</a>
            <input type="text" name="email" placeholder="Введите почту">
            <a>Введите пароль</a>
            <input type="password" name="password" placeholder="Введите пароль">
            <a style="color: #0000FF" href="/forgot_pass">Забыли пароль?</a>
            <button type="submit">Войти</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route('/menu')
def menu():
    html_content = '''
    <!DOCTYPE html>
    <html lang="ru">
      <head>
        <meta charset="utf-8">
        <title>Меню</title>
        <style>
          body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f2f2f2;
          }
          .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          }
          button {
            width: 220px;
            padding: 10px;
            margin-top: 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
          }
          button:hover {
            background-color: #0056b3;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h2>Вы успешно авторизовались</h2>
          <form action="/main">
            <button>Перейти к меню</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route('/main')
def main_part_menu():
    menu_items = {
        "main": [
            {"id": 1, "name": "Филе миньон с трюфельным соусом", "image_url": "https://via.placeholder.com/300x180?text=Филе+миньон", "price": 2200},
            {"id": 2, "name": "Утиная грудка с апельсиновым соусом", "image_url": "https://via.placeholder.com/300x180?text=Утиная+грудка", "price": 1800},
            {"id": 3, "name": "Лосось на гриле с икрой", "image_url": "https://via.placeholder.com/300x180?text=Лосось+на+гриле", "price": 2100},
            {"id": 10, "name": "Телятина sous-vide с грибным пюре", "image_url": "https://via.placeholder.com/300x180?text=Телятина", "price": 2400},
            {"id": 11, "name": "Ризотто с шафраном", "image_url": "https://via.placeholder.com/300x180?text=Ризотто", "price": 1600},
            {"id": 12, "name": "Стейк из тунца с каперсами", "image_url": "https://via.placeholder.com/300x180?text=Стейк+из+тунца", "price": 2300},
            {"id": 13, "name": "Агнёнок с розмарином", "image_url": "https://via.placeholder.com/300x180?text=Агнёнок", "price": 2500},
            {"id": 14, "name": "Курица sous-vide с пряным соусом", "image_url": "https://via.placeholder.com/300x180?text=Курица", "price": 1700},
            {"id": 15, "name": "Гребешки с цветной капустой", "image_url": "https://via.placeholder.com/300x180?text=Гребешки", "price": 2600},
        ],
        "desserts": [
            {"id": 4, "name": "Мильфей с клубничным кремом", "image_url": "https://via.placeholder.com/300x180?text=Мильфей", "price": 750},
            {"id": 5, "name": "Фондю из тёмного шоколада", "image_url": "https://via.placeholder.com/300x180?text=Фондю", "price": 850},
            {"id": 6, "name": "Торт Павлова", "image_url": "https://via.placeholder.com/300x180?text=Павлова", "price": 780},
        ],
        "drinks": [
            {"id": 7, "name": "Игристое вино Brut", "image_url": "https://via.placeholder.com/300x180?text=Brut", "price": 1500},
            {"id": 8, "name": "Фирменный коктейль Luxe", "image_url": "https://via.placeholder.com/300x180?text=Luxe+коктейль", "price": 900},
            {"id": 9, "name": "Свежевыжатый гранатовый сок", "image_url": "https://via.placeholder.com/300x180?text=Гранатовый+сок", "price": 600},
            {"id": 16, "name": "Домашний лимонад с мятой", "image_url": "https://via.placeholder.com/300x180?text=Лимонад", "price": 550},
            {"id": 17, "name": "Минеральная вода Voss", "image_url": "https://via.placeholder.com/300x180?text=Voss", "price": 450},
            {"id": 18, "name": "Эспрессо двойной", "image_url": "https://via.placeholder.com/300x180?text=Эспрессо", "price": 400},
        ]
    }

    html_content = '''<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <title>Меню Luxe Star</title>
    <style>
        /* Стили как у тебя */
        body { font-family: Arial, sans-serif; margin: 0; background: #f8f9fa; display: flex; }
        .sidebar { width: 220px; background: #343a40; color: white; padding-top: 40px; display: flex; flex-direction: column; align-items: center; height: 100vh; position: sticky; top: 0; }
        .sidebar button { width: 180px; margin: 10px 0; padding: 12px; font-size: 16px; background: transparent; color: white; border: 1px solid white; border-radius: 6px; cursor: pointer; transition: all 0.3s; }
        .sidebar button:hover, .sidebar button.active { background: white; color: #343a40; }
        .content { flex: 1; padding: 40px; }
        .menu { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
        .card { background: white; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; display: flex; flex-direction: column; }
        .card img { width: 100%; height: 180px; object-fit: cover; }
        .info { padding: 15px; text-align: center; }
        .info h4 { margin: 10px 0; font-size: 18px; }
        .info p { margin: 0; color: #444; }
        .info button { margin-top: 10px; padding: 8px 16px; font-size: 16px; border: none; border-radius: 4px; cursor: pointer; background: #28a745; color: white; }
        .info button:hover { background: #218838; }
        .cart { position: fixed; top: 20px; right: 20px; background: #007BFF; color: white; padding: 12px 20px; border-radius: 6px; cursor: pointer; z-index: 1000; }
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); justify-content: center; align-items: center; z-index: 999; }
        .modal-content { background: white; padding: 30px; border-radius: 8px; text-align: center; min-width: 300px; }
        .modal-content h3 { margin-bottom: 20px; }
        .modal-content p { margin: 10px 0; }
        .modal-content button, .modal-content a { margin-top: 10px; padding: 10px 20px; font-size: 16px; border: none; border-radius: 4px; text-decoration: none; display: inline-block; cursor: pointer; }
        .close-btn { background: #6c757d; color: white; margin-right: 10px; }
        .delivery-btn { background: #17a2b8; color: white; }
    </style>
</head>
<body>
<div class="sidebar">
    <button class="active" onclick="showCategory('main')">Основные блюда</button>
    <button onclick="showCategory('desserts')">Десерты</button>
    <button onclick="showCategory('drinks')">Напитки</button>
</div>

<div class="content">
    <div id="main" class="menu">
        {% for item in menu_items['main'] %}
        <div class="card" data-id="{{ item.id }}">
            <img src="{{ item.image_url }}" alt="{{ item.name }}">
            <div class="info">
                <h4>{{ item.name }}</h4>
                <p>{{ item.price }} ₽</p>
                <button onclick="addToCart({{ item.id }}, '{{ item.name }}', {{ item.price }}, this)">Добавить</button>
            </div>
        </div>
        {% endfor %}
    </div>

    <div id="desserts" class="menu" style="display:none;">
        {% for item in menu_items['desserts'] %}
        <div class="card" data-id="{{ item.id }}">
            <img src="{{ item.image_url }}" alt="{{ item.name }}">
            <div class="info">
                <h4>{{ item.name }}</h4>
                <p>{{ item.price }} ₽</p>
                <button onclick="addToCart({{ item.id }}, '{{ item.name }}', {{ item.price }}, this)">Добавить</button>
            </div>
        </div>
        {% endfor %}
    </div>

    <div id="drinks" class="menu" style="display:none;">
        {% for item in menu_items['drinks'] %}
        <div class="card" data-id="{{ item.id }}">
            <img src="{{ item.image_url }}" alt="{{ item.name }}">
            <div class="info">
                <h4>{{ item.name }}</h4>
                <p>{{ item.price }} ₽</p>
                <button onclick="addToCart({{ item.id }}, '{{ item.name }}', {{ item.price }}, this)">Добавить</button>
            </div>
        </div>
        {% endfor %}
    </div>
</div>

<div class="cart" onclick="toggleCart()">Корзина</div>
<div id="cartModal" class="modal">
    <div class="modal-content">
        <h3>Корзина</h3>
        <div id="cartItems">Корзина пуста</div>
        <div id="cartTotal"></div>
        <button class="close-btn" onclick="toggleCart()">Закрыть</button>
        <form action="/delivery">
            <button class="delivery-btn">Оформить заказ</button>
        </form>
    </div>
</div>

<script>
    const cart = {};

    function addToCart(id, name, price, btn) {
        if (!cart[id]) {
            cart[id] = { name, price, count: 1 };
            btn.textContent = "Добавлено";
            btn.style.backgroundColor = "#6c757d";
            btn.disabled = true;
        } else {
            cart[id].count += 1;
        }
        updateCartDisplay();
    }

    function removeFromCart(id, btn) {
        if (cart[id]) {
            cart[id].count -= 1;
            if (cart[id].count <= 0) {
                delete cart[id];
                const card = document.querySelector(`.card[data-id='${id}']`);
                if (card) {
                    const addButton = card.querySelector("button");
                    addButton.textContent = "Добавить";
                    addButton.style.backgroundColor = "#28a745";
                    addButton.disabled = false;
                }
            }
        }
        updateCartDisplay();
    }

    
    function updateCartDisplay() {
        const orderBtn = document.querySelector('.delivery-btn');
        if (orderBtn) {
            orderBtn.disabled = Object.keys(cart).length === 0;
        }
    
        const cartItems = document.getElementById('cartItems');
        const cartTotal = document.getElementById('cartTotal');
        let html = '';
        let total = 0;

        for (const id in cart) {
            const item = cart[id];
            html += `
                <div>
                    ${item.name} × ${item.count} — ${item.count * item.price} ₽
                    <button onclick="addToCart(${id}, '${item.name}', ${item.price}, this)">➕</button>
                    <button onclick="removeFromCart(${id}, this)">➖</button>
                </div>
            `;
            total += item.count * item.price;
        }

        cartItems.innerHTML = html || "Корзина пуста";
        cartTotal.textContent = total ? `Сумма: ${total} ₽` : "";
    }

    function toggleCart() {
        const modal = document.getElementById('cartModal');
        if (modal.style.display === 'flex') {
            modal.style.display = 'none';
        } else {
            updateCartDisplay();
            modal.style.display = 'flex';
        }
    }

    function showCategory(category) {
        ['main', 'desserts', 'drinks'].forEach(c => {
            document.getElementById(c).style.display = c === category ? 'grid' : 'none';
        });
        document.querySelectorAll('.sidebar button').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');
    }
</script>
</body>
</html>'''

    return render_template_string(html_content, menu_items=menu_items)


@app.route('/delivery', methods=['GET', 'POST'])
def delivery():
    html_content = '''
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Форма доставки</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
            .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            .form-group { margin-bottom: 20px; }
            label { display: block; margin-bottom: 8px; font-weight: bold; }
            input[type="text"], input[type="number"], select { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
            button { padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
            button:hover { background-color: #0056b3; }
            .error { color: red; font-size: 14px; margin-bottom: 20px; }
            .success { color: green; font-size: 14px; margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Форма доставки</h2>
            {% if error_message %}
                <div class="error">{{ error_message }}</div>
            {% endif %}
            {% if success_message %}
                <div class="success">{{ success_message }}</div>
            {% endif %}
            <form method="POST">
                <div class="form-group">
                    <label for="address">Адрес доставки</label>
                    <input type="text" id="address" name="address" placeholder="Введите адрес (Например:Улица 1-я Владимирская дом 9, регистр не учитывается)" required>
                </div>

                <div class="form-group">
                    <label for="door_code">Код от домофона</label>
                    <input type="text" id="door_code" name="door_code" placeholder="Введите код от домофона" required>
                </div>

                <div class="form-group">
                    <label for="payment_method">Способ оплаты</label>
                    <select id="payment_method" name="payment_method" required>
                        <option value="cash">Наличные</option>
                        <option value="cash_on_delivery">Картой при получении</option>
                        <option value="online">Картой онлайн</option>
                    </select>
                </div>

                <button type="submit">Заказать</button>
            </form>
        </div>
    </body>
    </html>
    '''

    if request.method == 'POST':
        address = request.form.get('address').strip()
        door_code = request.form.get('door_code').strip()
        payment_method = request.form.get('payment_method')
        if not address or not validate_address(address):
            error_message = 'Пожалуйста, введите корректный адрес с улицей, домом и номером дома.'
            return render_template_string(html_content, error_message=error_message)
        return render_template_string(html_content, success_message='Заказ успешно оформлен!')
    return render_template_string(html_content)


def validate_address(address):
    address_pattern = r"улица\s+[а-яА-ЯёЁ0-9\s-]+\s+дом\s+\d+"
    return bool(re.search(address_pattern, address.lower()))


if __name__ == '__main__':
    app.run(debug=True)
