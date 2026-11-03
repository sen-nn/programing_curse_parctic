import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

DB_PATH = 'app.db'


def get_connection():
    """Открывает соединение с базой и настраивает доступ к полям по имени."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # ← строки станут sqlite3.Row
    return conn


@app.route('/')
def index():
    # 1. Подключение
    conn = get_connection()
    cursor = conn.cursor()

    # 2. SELECT
    cursor.execute("SELECT id, title, status FROM tasks ORDER BY id")
    rows = cursor.fetchall()

    # 3. Закрытие (commit не нужен — данных не меняем)
    conn.close()

    # 4. Передача в шаблон
    return render_template('index.html', items=rows)


if __name__ == '__main__':
    app.run(debug=True, port=5000)