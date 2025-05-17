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
                <button class="login-btn">Войти в аккаунт и перетий к меню</button>
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
            {"id": 1, "name": "Филе миньон с трюфельным соусом", "image_url": "data:image/jpeg;base64,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", "price": 2200},
            {"id": 2, "name": "Утиная грудка с апельсиновым соусом", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTrj10HC4SUXDj4qau2w6OXsPqZBURPbLEr1w&s", "price": 1800},
            {"id": 3, "name": "Лосось на гриле с икрой", "image_url": "data:image/jpeg;base64,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", "price": 2100},
            {"id": 10, "name": "Телятина sous-vide с грибным пюре", "image_url": "data:image/jpeg;base64,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", "price": 2400},
            {"id": 11, "name": "Ризотто с шафраном", "image_url": "data:image/jpeg;base64,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", "price": 1600},
            {"id": 12, "name": "Стейк из тунца с каперсами", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpo8bafp_ECpByFjvZHa-8mG2OOJ0LD7W8sA&s", "price": 2300},
            {"id": 13, "name": "Агнёнок с розмарином", "image_url": "data:image/jpeg;base64,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", "price": 2500},
            {"id": 14, "name": "Курица sous-vide с пряным соусом", "image_url": "data:image/jpeg;base64,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", "price": 1700},
            {"id": 15, "name": "Гребешки с цветной капустой", "image_url": "data:image/jpeg;base64,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", "price": 2600},
        ],
        "desserts": [
            {"id": 4, "name": "Мильфей с клубничным кремом", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQj0agLTmj80sLe-uDrOv1RwTkpJz2hgoKiuA&s", "price": 750},
            {"id": 5, "name": "Фондю из шоколада с ягодами", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMrYPc4UryWsnGTUuo7NL55Skojm7CyHuRuw&s", "price": 850},
            {"id": 6, "name": "Торт Павлова", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSq-0Rog7bGqA56Lz3JnAYlmpIKfCIvvEkl1A&s", "price": 780},
        ],
        "drinks": [
            {"id": 7, "name": "Игристое вино Brut", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7Nrvis5T0HOJXw3o6-Kal0PCrssiTnahKBA&s", "price": 1500},
            {"id": 8, "name": "Фирменный коктейль Luxe", "image_url": "data:image/jpeg;base64,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", "price": 900},
            {"id": 9, "name": "Свежевыжатый гранатовый сок", "image_url": "data:image/jpeg;base64,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", "price": 600},
            {"id": 16, "name": "Домашний лимонад с мятой", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlkF9VfLCC5M-I2qyZpAr9gKuK71xSro8D-w&s", "price": 550},
            {"id": 17, "name": "Минеральная вода Voss", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwtcxrWt6PrTtDvcHKydv22bO1n0qzncKIHh_i90r9FzsAYdDRB1hOrLCZ3G3c5V2UqVw&usqp=CAU", "price": 450},
            {"id": 18, "name": "Эспрессо двойной", "image_url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93", "price": 400},
        ]
    }

    html_content = '''
    <!doctype html>
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