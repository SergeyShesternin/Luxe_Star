from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def log():
    html_content = '''
    <!doctype html>
    <html lang="en">
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
          h2 {
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
            margin-bottom: 20px;
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
        </style>
      </head>
      <body>
        <div class="container">
          <a>Войдите в аккаунт или<a>
          <a style="color: #0000FF" href="http://127.0.0.1:8080/reg">зарегистрируйтесь</a>
          <h3>Имя аккаунта</h3>
          <input type="text" placeholder="Введите имя аккаунта">
          <h3>Пароль</h3>
          <input type="text" placeholder="Введите пароль">
          <a style="color: #0000FF" href="http://127.0.0.1:8080/forgot_pass">Забыли пароль?</a>
          <form action="http://127.0.0.1:8080/menu">
            <button>Войти</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route('/reg')
def reg():
    html_content = '''
    <!doctype.html>
    <html lang=en>
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
          h2 {
            margin: 10px 0;
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
        </style>
      </head>
      <body>
        <div class="container">
          <a>Регистрация</a>
          <h3>Введите почту</h3>
          <input type="text" placeholder="Введите почту">
          <h3>Пароль</h3>
          <input type="text" placeholder="Введите пароль">
          <h3>Повторите пароль</h3>
          <input type="text" placeholder="Введите пароль повторно">
          <h3>Ваше имя</h3>
          <input type="text" placeholder="Введите ваше имя">
          <form action="http://127.0.0.1:8080/menu">
            <button>Зарегистрироваться</button>
          </form>
        </div>
      </body>
    '''
    return render_template_string(html_content)


@app.route('/forgot_pass')
def forgot_pass():
    html_content = '''
        <!doctype.html>
        <html lang=en>
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
          h2 {
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
            margin-bottom: 20px;
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
        </style>
          </head>
          <body>
            <div>
              <a>Ошибка</a>
              <h3>Так как мы криворукие идиоты вам придется создать новый аккаунт</h3>
              <form action="http://127.0.0.1:8080/reg">
                <button>Зарегистрироваться</button>
              </form>
            </div>
          </body>
        '''
    return render_template_string(html_content)


@app.route('/menu')
def menu():
    html_content = '''
        <!doctype.html>
            <html lang=en>
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
              h2 {
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
                margin-bottom: 20px;
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
            </style>
              </head>
              <body>
                <div>
                  <a>Выуспешно авторизовались</a>
                  <form action="http://127.0.0.1:8080/first">
                    <button>Перейти к меню</button>
                  </form>
                </div>
              </body>
            '''
    return render_template_string(html_content)


@app.route('/first')
def first_part_menu():
    html_content = '''
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <title>Меню доставки еды</title>
            <style>
              body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
              }
              .main-container {
                display: flex;
                height: 100vh;
              }
              .sidebar {
                width: 200px;
                background-color: #ffffff;
                padding: 20px;
                box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
              }
              .sidebar h3 {
                margin-top: 0;
                font-size: 18px;
                margin-bottom: 15px;
              }
              .tab {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                text-align: left;
              }
              .tab:hover {
                background-color: #0056b3;
              }
              .content-area {
                flex-grow: 1;
                padding: 20px 40px 20px 20px;
                overflow-y: auto;
              }
              .grid-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                max-width: 1200px;
                margin: 0 auto; 
              }
              .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 10px;
                height: 280px;
              }
              .card img {
                width: 100%;
                height: 180px;
                object-fit: cover;
                border-radius: 6px;
              }
              .card button {
                margin-top: 10px;
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
              }
              .card button:hover {
                background-color: #1e7e34;
              }
            </style>
          </head>
          <body>
            <div class="main-container">
              <div class="sidebar">
                <h3>Категории</h3>
                <form action="http://127.0.0.1:8080/first">
                  <button class="tab">Вкладка 1</button>
                </form>
                <form action="http://127.0.0.1:8080/second">
                  <button class="tab">Вкладка 2</button>
                </form>
                <form action="http://127.0.0.1:8080/third">
                  <button class="tab">Вкладка 3</button>
                </form>
              </div>
              <div class="content-area">
                <div class="grid-container">
                  {% for i in range(9) %}
                  <div class="card">
                    <img src="https://via.placeholder.com/300x180" alt="Изображение">
                    <button>Добавить в корзину</button>
                  </div>
                  {% endfor %}
                </div>
              </div>
            </div>
          </body>
        </html>
        '''
    return render_template_string(html_content)


@app.route('/second')
def second_part_menu():
    html_content = '''
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <title>Меню доставки еды</title>
            <style>
              body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
              }
              .main-container {
                display: flex;
                height: 100vh;
              }
              .sidebar {
                width: 200px;
                background-color: #ffffff;
                padding: 20px;
                box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
              }
              .sidebar h3 {
                margin-top: 0;
                font-size: 18px;
                margin-bottom: 15px;
              }
              .tab {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                text-align: left;
              }
              .tab:hover {
                background-color: #0056b3;
              }
              .content-area {
                flex-grow: 1;
                padding: 20px 40px 20px 20px;
                overflow-y: auto;
              }
              .grid-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                max-width: 1200px;
                margin: 0 auto; 
              }
              .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 10px;
                height: 280px;
              }
              .card img {
                width: 100%;
                height: 180px;
                object-fit: cover;
                border-radius: 6px;
              }
              .card button {
                margin-top: 10px;
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
              }
              .card button:hover {
                background-color: #1e7e34;
              }
            </style>
          </head>
          <body>
            <div class="main-container">
              <div class="sidebar">
                <h3>Категории</h3>
                <form action="http://127.0.0.1:8080/first">
                  <button class="tab">Вкладка 1</button>
                </form>
                <form action="http://127.0.0.1:8080/second">
                  <button class="tab">Вкладка 2</button>
                </form>
                <form action="http://127.0.0.1:8080/third">
                  <button class="tab">Вкладка 3</button>
                </form>
              </div>
              <div class="content-area">
                <div class="grid-container">
                  {% for i in range(6) %}
                  <div class="card">
                    <img src="https://via.placeholder.com/300x180" alt="Изображение">
                    <button>Добавить в корзину</button>
                  </div>
                  {% endfor %}
                </div>
              </div>
            </div>
          </body>
        </html>
        '''
    return render_template_string(html_content)


@app.route('/third')
def third_part_menu():
    html_content = '''
        <!doctype html>
        <html lang="ru">
          <head>
            <meta charset="utf-8">
            <title>Меню доставки еды</title>
            <style>
              body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
              }
              .main-container {
                display: flex;
                height: 100vh;
              }
              .sidebar {
                width: 200px;
                background-color: #ffffff;
                padding: 20px;
                box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
              }
              .sidebar h3 {
                margin-top: 0;
                font-size: 18px;
                margin-bottom: 15px;
              }
              .tab {
                margin-bottom: 10px;
                padding: 10px;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                width: 100%;
                text-align: left;
              }
              .tab:hover {
                background-color: #0056b3;
              }
              .content-area {
                flex-grow: 1;
                padding: 20px 40px 20px 20px;
                overflow-y: auto;
              }
              .grid-container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 20px;
                max-width: 1200px;
                margin: 0 auto; 
              }
              .card {
                background-color: white;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                padding: 10px;
                height: 280px;
              }
              .card img {
                width: 100%;
                height: 180px;
                object-fit: cover;
                border-radius: 6px;
              }
              .card button {
                margin-top: 10px;
                padding: 10px;
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
              }
              .card button:hover {
                background-color: #1e7e34;
              }
            </style>
          </head>
          <body>
            <div class="main-container">
              <div class="sidebar">
                <h3>Категории</h3>
                <form action="http://127.0.0.1:8080/first">
                  <button class="tab">Вкладка 1</button>
                </form>
                <form action="http://127.0.0.1:8080/second">
                  <button class="tab">Вкладка 2</button>
                </form>
                <form action="http://127.0.0.1:8080/third">
                  <button class="tab">Вкладка 3</button>
                </form>
              </div>
              <div class="content-area">
                <div class="grid-container">
                  {% for i in range(3) %}
                  <div class="card">
                    <img src="https://via.placeholder.com/300x180" alt="Изображение">
                    <button>Добавить в корзину</button>
                  </div>
                  {% endfor %}
                </div>
              </div>
            </div>
          </body>
        </html>
        '''
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')