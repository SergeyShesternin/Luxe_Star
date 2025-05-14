from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def main():
    html_content = '''
       <!DOCTYPE html>
       <html lang="ru">
         <head>
           <meta charset="utf-8">
           <title>Главная</title>
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
               background-color: #007BFF;
               color: white;
               border: none;
               border-radius: 4px;
               cursor: pointer;
               font-size: 16px;
               position: absolute; /* Абсолютное позиционирование для кнопки */
               top: 10px;  /* Отступ сверху */
               right: 10px; /* Отступ слева */
             }
             button:hover {
               background-color: #0056b3;
             }
           </style>
         </head>
         <body>
           <div class="container">
             <form action='/log'>
               <button>Войти в аккаунт</button>
             </form>
           </div>
         </body>
       </html>
       '''
    return render_template_string(html_content)


@app.route('/log')
def log():
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
          <a>Войдите в аккаунт или</a>
          <a style="color: #0000FF" href="/reg">зарегистрируйтесь</a>
          <h3>Имя аккаунта</h3>
          <input type="text" placeholder="Введите имя аккаунта">
          <h3>Пароль</h3>
          <input type="password" placeholder="Введите пароль">
          <a style="color: #0000FF" href="/forgot_pass">Забыли пароль?</a>
          <form action="/menu">
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
          <a>Введите почту</a>
          <input type="text" placeholder="Введите почту">
          <a>Введите пароль</a>
          <input type="password" placeholder="Введите пароль">
          <a>Повторите пароль</a>
          <input type="password" placeholder="Повторите пароль">
          <a>Ваше имя</a>
          <input type="text" placeholder="Ваше имя">
          <form action="/menu">
            <button>Зарегистрироваться</button>
          </form>
        </div>
      </body>
    </html>
    '''
    return render_template_string(html_content)


@app.route('/forgot_pass')
def forgot_pass():
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
          <h2>Ошибка</h2>
          <p>Так как мы криворукие идиоты, вам придётся создать новый аккаунт</p>
          <form action="/reg">
            <button>Зарегистрироваться</button>
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
    menu_items = [
        {"id": 1, "name": "Пицца Маргарита", "image_url": "https://via.placeholder.com/300x180?text=Пицца+Маргарита", "price": 450},
        {"id": 2, "name": "Бургер с говядиной", "image_url": "https://via.placeholder.com/300x180?text=Бургер", "price": 350},
        {"id": 3, "name": "Суши сет", "image_url": "https://via.placeholder.com/300x180?text=Суши+сет", "price": 1200},
        {"id": 4, "name": "Паста Карбонара", "image_url": "https://via.placeholder.com/300x180?text=Паста", "price": 500},
        {"id": 5, "name": "Салат Цезарь", "image_url": "https://via.placeholder.com/300x180?text=Цезарь", "price": 300},
        {"id": 6, "name": "Шашлык из курицы", "image_url": "https://via.placeholder.com/300x180?text=Шашлык", "price": 600},
        {"id": 7, "name": "Рамен", "image_url": "https://via.placeholder.com/300x180?text=Рамен", "price": 550},
        {"id": 8, "name": "Лазанья", "image_url": "https://via.placeholder.com/300x180?text=Лазанья", "price": 470},
        {"id": 9, "name": "Десерт Тирамису", "image_url": "https://via.placeholder.com/300x180?text=Тирамису", "price": 250},
    ]

    html_content = '''
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <title>Меню</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                background-color: #f5f5f5;
            }
            .header {
                display: flex;
                justify-content: flex-end;
                padding: 20px;
                background-color: #fff;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                position: sticky;
                top: 0;
                z-index: 100;
            }
            .cart-btn {
                background-color: #007BFF;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .menu {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
                padding: 40px;
            }
            .card {
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                overflow: hidden;
                display: flex;
                flex-direction: column;
            }
            .card img {
                width: 100%;
                height: 180px;
                object-fit: cover;
            }
            .info {
                padding: 15px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .info h4 {
                margin: 10px 0;
            }
            .info p {
                margin: 0;
                color: #444;
            }
            .info button {
                margin-top: 10px;
                padding: 8px 16px;
                font-size: 16px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            .add-btn {
                background-color: #28a745;
                color: white;
            }
            .remove-btn {
                background-color: #dc3545;
                color: white;
            }
            .modal {
                display: none;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0,0,0,0.5);
                justify-content: center;
                align-items: center;
            }
            .modal-content {
                background: white;
                padding: 30px;
                border-radius: 8px;
                min-width: 300px;
                text-align: center;
            }
            .modal-content button,
            .modal-content a {
                margin-top: 10px;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
                text-decoration: none;
                display: inline-block;
            }
            .close-btn {
                background-color: #6c757d;
                color: white;
                margin-right: 10px;
            }
            .delivery-btn {
                background-color: #17a2b8;
                color: white;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <button class="cart-btn" onclick="toggleCart()">Корзина</button>
        </div>

        <div class="menu">
            {% for item in menu_items %}
            <div class="card" data-id="{{ item.id }}">
                <img src="{{ item.image_url }}" alt="{{ item.name }}">
                <div class="info">
                    <h4>{{ item.name }}</h4>
                    <p>{{ item.price }} ₽</p>
                    <button class="add-btn" onclick="toggleItem({{ item.id }}, '{{ item.name }}', {{ item.price }}, this)">+</button>
                </div>
            </div>
            {% endfor %}
        </div>

        <div class="modal" id="cartModal">
            <div class="modal-content" id="cartContent">
                <h3>Ваша корзина</h3>
                <p id="cartItems"></p>
                <p id="cartTotal"></p>
                <button class="close-btn" onclick="toggleCart()">Закрыть</button>
                <a href="/delivery" class="delivery-btn">Перейти к доставке</a>
            </div>
        </div>

        <script>
            const cart = {};
            function toggleItem(id, name, price, btn) {
                if (cart[id]) {
                    delete cart[id];
                    btn.textContent = '+';
                    btn.className = 'add-btn';
                } else {
                    cart[id] = { name, price };
                    btn.textContent = '-';
                    btn.className = 'remove-btn';
                }
            }

            function toggleCart() {
                const modal = document.getElementById('cartModal');
                const cartItems = document.getElementById('cartItems');
                const cartTotal = document.getElementById('cartTotal');
                if (modal.style.display === 'flex') {
                    modal.style.display = 'none';
                } else {
                    let text = '';
                    let total = 0;
                    let count = 0;
                    for (const id in cart) {
                        count++;
                        text += `- ${cart[id].name} — ${cart[id].price} ₽<br>`;
                        total += cart[id].price;
                    }
                    cartItems.innerHTML = count ? text : 'Корзина пуста';
                    cartTotal.textContent = count ? `Сумма заказа: ${total} ₽` : '';
                    modal.style.display = 'flex';
                }
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content, menu_items=menu_items)




@app.route('/delivery')
def delivery():
    html_content = '''
    '''
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(debug=True)
