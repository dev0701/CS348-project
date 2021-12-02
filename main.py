#main.py
from flask import Flask, jsonify, request, render_template, flash, session, abort
from flask import session as login_session
from flaskext.mysql import MySQL
import os

app = Flask(__name__)
app.secret_key = "totallysupersecret"
mysql = MySQL()

#MySQL config
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Zer0cool'
app.config['MYSQL_DATABASE_DB'] = 'cs348project'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/login", methods=['POST','GET'])
def login():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return render_template("managerInfo.html")

@app.route("/logout", methods=['POST','GET'])
def logout():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        session['logged_in'] = False
        return login()

@app.route("/search", methods=['POST','GET'])
def search():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
       return render_template("search.html") 

@app.route("/authenticate", methods=['POST','GET'])
def authenticate():
    if auth_user(request.form['employee_id'], request.form['password']) != "Authentication Failed":
        session['logged_in'] = True
        session['id'] = request.form['employee_id']
        curr_user = auth_user(request.form['employee_id'], request.form['password'])
        print(curr_user, flush=True)
        return login()
    else:
        flash('The customer username or password is incorrect')
    return login()

def auth_user(employee_id, password):
    conn = mysql.connect()
    with conn.cursor() as cursor: 
        result = cursor.execute('SELECT * FROM Employee WHERE employee_id = %s and password = %s', (employee_id, password))
        customers = cursor.fetchall()
        if result > 0:
            got_customers = "auth pass"
        else:
            got_customers = "Authentication Failed"
    conn.close()
    return got_customers

if __name__ == '__main__':
    app.run(debug=True)