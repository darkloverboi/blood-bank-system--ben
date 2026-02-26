print("\u2705 app.py is running...")

from flask import Flask, render_template, request, redirect, url_for, session, make_response
import sqlite3
import csv

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Initialize database
def init_db():
    conn = sqlite3.connect('database/donors.db')
    c = conn.cursor()

    # Donors Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            blood_group TEXT,
            contact TEXT,
            email TEXT,
            address TEXT
        )
    ''')

    # Requests Table
    c.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact TEXT,
            blood_group TEXT,
            units INTEGER,
            hospital TEXT,
            urgency TEXT
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register_donor():
    if request.method == 'POST':
        data = (
            request.form['name'], request.form['age'], request.form['gender'],
            request.form['blood_group'], request.form['contact'],
            request.form['email'], request.form['address']
        )
        conn = sqlite3.connect('database/donors.db') 
        cur = conn.cursor()
        cur.execute('INSERT INTO donors (name, age, gender, blood_group, contact, email, address) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('register.html')

@app.route('/donors')
def manage_donors():
    blood_group = request.args.get('group')
    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()

    if blood_group:
        cur.execute('SELECT * FROM donors WHERE blood_group = ?', (blood_group,))
    else:
        cur.execute('SELECT * FROM donors')

    donors = cur.fetchall()
    conn.close()
    return render_template('donors.html', donors=donors)

@app.route('/request', methods=['GET', 'POST'])
def request_blood():
    if request.method == 'POST':
        data = (
            request.form['name'], request.form['contact'],
            request.form['blood_group'], request.form['units'],
            request.form['hospital'], request.form['urgency']
        )
        conn = sqlite3.connect('database/donors.db')
        c = conn.cursor()
        c.execute("INSERT INTO requests (name, contact, blood_group, units, hospital, urgency) VALUES (?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('request.html')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            session['admin_logged_in'] = True
            return redirect('/admin/dashboard')
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    return render_template('admin_login.html')

@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect('/admin/login')

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'admin_logged_in' not in session:
        return redirect('/admin/login')

    try:
        conn = sqlite3.connect('database/donors.db')
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*) FROM donors')
        total_donors = cur.fetchone()[0]
        cur.execute('SELECT COUNT(*) FROM requests')
        total_requests = cur.fetchone()[0]
        conn.close()

        return render_template('admin_dashboard.html', total_donors=total_donors, total_requests=total_requests)

    except Exception as e:
        print("\u274c ERROR in dashboard:", e)
        return "<h2>Error loading dashboard</h2>"

@app.route('/admin/inventory')
def admin_inventory():
    if 'admin_logged_in' not in session:
        return redirect('/admin/login')

    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()
    cur.execute('SELECT blood_group, COUNT(*) FROM donors GROUP BY blood_group')
    rows = cur.fetchall()
    conn.close()

    stock = {group: count for group, count in rows}
    all_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    for group in all_groups:
        stock.setdefault(group, 0)

    return render_template('admin_inventory.html', stock=stock)

@app.route('/admin/requests')
def view_requests():
    if 'admin_logged_in' not in session:
        return redirect('/admin/login')

    conn = sqlite3.connect('database/donors.db')
    c = conn.cursor()
    c.execute("SELECT * FROM requests")
    data = c.fetchall()
    conn.close()
    return render_template('admin_requests.html', requests=data)

@app.route('/admin/delete_donor/<int:donor_id>', methods=['POST'])
def delete_donor(donor_id):
    if 'admin_logged_in' not in session:
        return redirect('/admin/login')

    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM donors WHERE id = ?', (donor_id,))
    conn.commit()
    conn.close()
    return redirect('/donors')

@app.route('/admin/delete_request/<int:req_id>', methods=['POST'])
def delete_request(req_id):
    if 'admin_logged_in' not in session:
        return redirect('/admin/login')

    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM requests WHERE id = ?', (req_id,))
    conn.commit()
    conn.close()
    return redirect('/admin/requests')

@app.route('/admin/export_donors')
def export_donors():
    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM donors")
    data = cur.fetchall()
    conn.close()

    output = "ID,Name,Age,Gender,Blood Group,Contact,Email,Address\n"
    for d in data:
        output += ",".join([str(field) for field in d]) + "\n"

    response = make_response(output)
    response.headers["Content-Disposition"] = "attachment; filename=donors.csv"
    response.headers["Content-type"] = "text/csv"
    return response

@app.route('/admin/export_requests')
def export_requests():
    conn = sqlite3.connect('database/donors.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM requests")
    data = cur.fetchall()
    conn.close()

    output = "ID,Name,Contact,Blood Group,Units,Hospital,Urgency\n"
    for r in data:
        output += ",".join([str(field) for field in r]) + "\n"

    response = make_response(output)
    response.headers["Content-Disposition"] = "attachment; filename=requests.csv"
    response.headers["Content-type"] = "text/csv"
    return response

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
