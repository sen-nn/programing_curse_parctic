from flask import Flask

# Создаём приложение. __name__ — имя текущего модуля;
# Flask использует его, чтобы найти папку templates рядом с файлом.
app = Flask(__name__)


@app.route('/')
def index():
    return """
    <html>
        <head><title>Список задач</title></head>
        <body>
            <h1>Мой список задач</h1>
            <p>Скоро здесь будет список задач из базы данных.</p>
        </body>
    </html>
    """
@app.route('/about')
def about():
    return "Это учебный список задач на Flask. Практическая работа №3."


if __name__ == '__main__':
    # debug=True — автоперезагрузка + подробные ошибки
    # port=5000 — стандартный порт Flask
    app.run(debug=True, port=5000)