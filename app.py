from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_data', methods=['POST'])
def save_data():
    try:
        data = request.get_json()

        # Connect to SQLite database (create one if not exists)
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                price REAL,
                location TEXT
            )
        ''')

        # Insert data into the database
        cursor.execute('INSERT INTO items (name, price, location) VALUES (?, ?, ?)',
                       (data['name'], data['price'], data['location']))
        conn.commit()
        conn.close()

        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)