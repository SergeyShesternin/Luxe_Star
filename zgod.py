from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/log')
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
          <form action="http://127.0.0.1:8080/chats">
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
          <h3>Имя аккаунта (нужен для входа в аккаунт)</h3>
          <input type="text" placeholder="Введите имя аккаунта">
          <h3>Пароль</h3>
          <input type="text" placeholder="Введите пароль">
          <h3>Повторите пароль</h3>
          <input type="text" placeholder="Введите пароль повторно">
          <h3>Ваше имя (его будут видеть другие пользователи)</h3>
          <input type="text" placeholder="Введите имя аккаунта">
          <h3>Ваше имя (его будут видеть другие пользователи)</h3>
          <input type="text" placeholder="Введите ваше имя">
          <h3>Укажите сколько вам лет</h3>
          <input type="range" min="10" max="50" step="1" value="15">
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
            color: #007BFF;
            text-decoration: none;
          }
          a:hover {
            text-decoration: underline;
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
              Манака манака манака зйцвцйвцйвцйвцйв однако
            </div>
          </body>
        '''
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')