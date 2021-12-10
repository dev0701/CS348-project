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
            if(position[0][0] == 'manager' or position[0][0] == 'Manager'):
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

@app.route("/search", methods=['POST','GET'])
def search():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
       if request.method == "POST":
            print('post method')
            form = request.form
            search_value = form['search_string']
            print(search_value)
            conn = mysql.connect()
            with conn.cursor() as cursor: 
                result = cursor.execute('SELECT DISTINCT * FROM Employee WHERE employee_id = %s OR first_name = %s OR last_name = %s OR position = %s OR salary = %s OR department_id = %s OR city = %s', (search_value,search_value,search_value,search_value,search_value,search_value,search_value ))
            data = cursor.fetchall()
            print(data)       
            conn.close()
            return render_template("search.html", data=data)       
    return render_template("search.html")

@app.route("/edit", methods=['POST','GET'])
def edit():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
       if request.method == "POST":
            print('post method')
            form = request.form
            search_value = form['search_string']
            print(search_value)
            conn = mysql.connect()
            with conn.cursor() as cursor: 
                result = cursor.execute('SELECT DISTINCT * FROM Employee WHERE employee_id = %s OR first_name = %s OR last_name = %s OR position = %s OR salary = %s OR department_id = %s OR city = %s', (search_value,search_value,search_value,search_value,search_value,search_value,search_value ))
            data = cursor.fetchall()
            print(data)       
            conn.close()
            return render_template("edit.html", data=data)       
    return render_template("edit.html")

@app.route("/edit_employee", methods=['POST','GET'])
def edit_employee_form():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        if request.method == "POST":
            print('post method')
            search_string = request.form['action']
            conn = mysql.connect()
            with conn.cursor() as cursor: 
                result = cursor.execute('SELECT DISTINCT * FROM Employee WHERE employee_id = %s ',(search_string))
            data = cursor.fetchall()  
            session['emp_id'] = data[0][0]   
            conn.close()
            return render_template("edit_employee.html", data=data)       
    return render_template("edit.html")
  
#edit employee
@app.route("/employee_edited", methods=['POST','GET'])
def edit_employee():
    conn = mysql.connect()
    with conn.cursor() as cursor:
        emp_id = session.get('emp_id', None)
        result = cursor.execute('UPDATE EMPLOYEE SET first_name = %s, last_name = %s, password = %s, salary = %s, city = %s, position = %s, department_id = %s WHERE employee_id = %s ', (request.form['first-name'], request.form['last-name'], request.form['password'], request.form['salary'], request.form['city-name'], request.form['position'], request.form['dept-id'], emp_id,))
        conn.commit()
        if result > 0:
            return login()
        else:
            useradded = 0
    conn.close()
    return edit_employee_form()


    
            
        
        

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