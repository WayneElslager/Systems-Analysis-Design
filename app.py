from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(app.instance_path, 'hotel.db')

# --- Database Helpers ---

def get_db():
    if 'db' not in g:
        os.makedirs(app.instance_path, exist_ok=True)
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            checkin     TEXT    NOT NULL,
            checkout    TEXT    NOT NULL,
            room_type   TEXT    NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

# --- Routes ---

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        name      = request.form['name'].strip()
        checkin   = request.form['checkin']
        checkout  = request.form['checkout']
        room_type = request.form['room_type']

        # Basic validation
        errors = []
        if not name:
            errors.append('Name is required.')
        if not checkin:
            errors.append('Check-in date is required.')
        if not checkout:
            errors.append('Check-out date is required.')
        if checkin and checkout and checkin >= checkout:
            errors.append('Check-out date must be after check-in date.')

        if errors:
            return render_template('reservation.html', errors=errors,
                                   name=name, checkin=checkin,
                                   checkout=checkout, room_type=room_type)

        db = get_db()
        db.execute(
            'INSERT INTO reservations (name, checkin, checkout, room_type) VALUES (?, ?, ?, ?)',
            (name, checkin, checkout, room_type)
        )
        db.commit()
        return redirect(url_for('confirmation',
                                name=name,
                                checkin=checkin,
                                checkout=checkout,
                                room_type=room_type))

    return render_template('reservation.html', errors=[])


@app.route('/confirmation')
def confirmation():
    name      = request.args.get('name', '')
    checkin   = request.args.get('checkin', '')
    checkout  = request.args.get('checkout', '')
    room_type = request.args.get('room_type', '')
    return render_template('confirmation.html',
                           name=name, checkin=checkin,
                           checkout=checkout, room_type=room_type)


@app.route('/manager')
def manager():
    db = get_db()
    reservations = db.execute(
        'SELECT * FROM reservations ORDER BY created_at DESC'
    ).fetchall()
    return render_template('manager.html', reservations=reservations)


@app.route('/manager/delete/<int:reservation_id>', methods=['POST'])
def delete_reservation(reservation_id):
    db = get_db()
    db.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
    db.commit()
    return redirect(url_for('manager'))


# --- Entry Point ---

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
