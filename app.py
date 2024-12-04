from flask import Flask, render_template, request, redirect, url_for, flash
from config import get_db_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Flash mesajları için

# Ana Sayfa
@app.route('/')
def index():
    return render_template('index.html')

# Arıza Ekleme Sayfası
@app.route('/add_fault', methods=['GET', 'POST'])
def add_fault():
    if request.method == 'POST':
        robot_name = request.form['robot_name']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        fault_reason = request.form['fault_reason']
        changed_part = request.form['changed_part']
        downtime = float(request.form['downtime'])
        lost_production = int(request.form['lost_production'])

        # Veritabanına ekleme
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO faults (robot_name, start_time, end_time, fault_reason, changed_part, downtime, lost_production)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (robot_name, start_time, end_time, fault_reason, changed_part, downtime, lost_production))
        connection.commit()

        # İstatistikleri güncelleme
        cursor.execute("""
            INSERT INTO statistics (robot_name, total_downtime, total_lost_production)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
            total_downtime = total_downtime + %s,
            total_lost_production = total_lost_production + %s
        """, (robot_name, downtime, lost_production, downtime, lost_production))
        connection.commit()
        connection.close()

        flash("Arıza başarıyla eklendi!", "success")
        return redirect(url_for('index'))

    return render_template('add_fault.html')

# İstatistik Görüntüleme Sayfası
@app.route('/view_stats')
def view_stats():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM statistics")
    stats = cursor.fetchall()
    connection.close()

    return render_template('view_stats.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True)
