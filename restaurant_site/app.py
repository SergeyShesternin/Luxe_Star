from flask import Flask, render_template
#импорт библиотек

app = Flask(__name__) #запускаем фласк

@app.route('/')
def home():
    return render_template('index.html') #главная страница

@app.route('/menu')
def menu():
    return render_template('menu.html') #меню

@app.route('/services')
def services():
    return render_template('services.html') #услуги

@app.route('/contacts')
def contacts():
    return render_template('contacts.html') #контакты

if __name__ == '__main__':
    app.run(debug=True)
    #конец