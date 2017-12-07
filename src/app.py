from flask import Flask, render_template, send_file, request
import time
import datetime
from src.common.database import SQL

app = Flask(__name__)
app.secret_key = "Amy" # The way to make request more secure


@app.route('/')
def home_template():
    return render_template('home.html')


@app.route('/download')
def download_template():
    return render_template('download.html')


@app.route('/show_history')
def show_template():
    sql = "SELECT * from info"
    infos = SQL().select(sql=sql)
    return render_template('report.html', infos=infos)


@app.route('/csv_test', methods=['POST'])
def file_return():
    delay = request.form['delay']
    t1 = datetime.datetime.now()
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    user_agent = user_agent.encode('utf-8')[:47]
    sql = "INSERT INTO info (delay, client_ip, user_agent) VALUES (%s, %s, %s) "
    SQL().update(sql, delay, client_ip, user_agent)
    t2 = datetime.datetime.now()
    elapsed = int((t2-t1).seconds)
    if elapsed < int(delay):
        time.sleep(int(delay) - int(elapsed))

    return send_file('static/assets/Sample.csv', attachment_filename='Sample.csv',
                     as_attachment=True)


if __name__ == '__main__':
    app.run(threaded=True)