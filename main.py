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

@app.route("/authenticate", methods=['POST','GET'])
def authenticate():
    if auth_user(request.form['employee_id'], request.form['password']) != "Authentication Failed":
        session['logged_in'] = True
        session['id'] = request.form['employee_id']
        conn = mysql.connect()
        with conn.cursor() as cursor:
            result = cursor.execute('SELECT position FROM Employee WHERE employee_id = %s', (session['id']))
            position = cursor.fetchall()
            result = cursor.execute('SELECT * FROM Employee WHERE employee_id = %s', (session['id']))
            data = cursor.fetchall()
            if(position[0][0] == 'manager'):
                return render_template("managerInfo.html", data = data)
            else:
                return render_template("userInfo.html", data = data)
    else:
        flash('The customer username or password is incorrect')
    return login()

def auth_user(employee_id, password):
    conn = mysql.connect()
    with conn.cursor() as cursor: 
        result = cursor.execute('SELECT * FROM Employee WHERE employee_id = %s and password = %s', (employee_id, password))
        user = cursor.fetchall()
        if result > 0:
            got_user= "auth pass"
        else:
            got_user= "Authentication Failed"
    conn.close()
    return got_user

@app.route("/adduser", methods=['POST','GET'])
def addUserForm():
    return render_template("addUser.html")

@app.route("/useradded", methods=['POST','GET'])
def addUser():
    conn = mysql.connect()
    with conn.cursor() as cursor: 
        result = cursor.execute('INSERT INTO `Employee` (`employee_id`, `first_name`,`last_name`,`position`,`salary`,`city`,`department_id`,`password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(request.form['employee-id'],request.form['first-name'],request.form['last-name'],request.form['position'],request.form['salary'],request.form['city-name'],request.form['dept-id'],request.form['password']))
        conn.commit()
        if result > 0:
            return login()
        else:
            useradded = 0
    conn.close()
    return addUserForm()
    
if __name__ == '__main__':
    app.run(debug=True)