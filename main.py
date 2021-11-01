#main.py
from flask import Flask, jsonify, request, render_template, flash, session, abort
from flask import session as login_session
from db import auth_user
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/login", methods=['POST','GET'])
def login():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return "You are already logged in."

@app.route("/authenticate", methods=['POST','GET'])
def authenticate():
    if auth_user(request.form['employee_id'], request.form['password']) != "Authentication Failed":
        session['logged_in'] = True
        session['id'] = request.form['employee_id']
        return login()
    else:
        flash('The customer username or password is incorrect')
    return login()

if __name__ == '__main__':
    app.run(debug=True)