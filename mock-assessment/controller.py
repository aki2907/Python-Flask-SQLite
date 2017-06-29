#!usr/bin/env python3

import os
from flask import Flask, render_template, redirect, url_for, request, flash
from wtforms import Form, TextField, StringField, TextAreaField, BooleanField, PasswordField, fields, validators
import model

app = Flask(__name__)
app.config['SECRET_KEY'] = '9876543210'
username="aki"

@app.route('/')
def show_homepage():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('my_page'))
    return render_template('admin.html', error=error)

class Register(Form):
    username = StringField('Username : ', [validators.DataRequired()])
    password = PasswordField('Password : ', [validators.DataRequired()])

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = Register(request.form)
    if request.method == 'POST':
        if form.validate() == True:
            global username
            username = request.form['username']
            password = request.form['password']
            model.add_user(username,password)
            return redirect(url_for('show_account'))
        else:
            return render_template('registration.html', form=form)
    elif request.method == 'GET':
        return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        submitted_username   = request.form.get('username')
        submitted_password   = request.form.get('password')
        objectified_username = model.Login.lookup_username(submitted_username)
        objectified_password = model.Login.lookup_password(submitted_username)
        model.Login(objectified_username, objectified_password)
        if request.form['username'] != objectified_username or request.form['password'] != objectified_password:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('show_account'))
    return render_template('login.html', error=error)

class Account(Form):
    fname = StringField('First Name : ', [validators.DataRequired()])
    lname = StringField('Last Name : ', [validators.DataRequired()])
    dob = StringField('Date of Birth : ', [validators.DataRequired()])
    phone_num = StringField('Phone Number : ', [validators.DataRequired()])
    address = TextAreaField('Address : ', [validators.DataRequired()])

@app.route('/account', methods=['GET', 'POST'])
def show_account():
    global username
    form = Account(request.form)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        phone_num = request.form['phone_num']
        address = request.form['address']
        model.insert_account_details(username, fname, lname, dob, phone_num, address)
        return redirect(url_for('my_page'))
    elif request.method == 'GET':
        return render_template('account.html', form=form)

@app.route('/my_page')
def my_page():
    return render_template('my_page.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
