

from ctypes import c_ssize_t
from pydoc import render_doc
from re import M, template

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template , request , redirect, url_for, session, Response
from datetime import datetime
import mysql.connector
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re



app = Flask(__name__)
app.secret_key= 'your secret key'
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'missingperson'
app.config["MYSQL_CURSORCLASS"]=""
mysql= MySQL(app)


@app.route("/mini", methods= ['GET', 'POST'])
def mini():
    global data
    msg = ''
    if request.method== 'POST' and 'first_name' in request.form and 'last_name' in request.form and 'found_location' in request.form and 'email' in request.form and 'phone_num' in request.form and 'date_found' in request.form:
        first_name= request.form['first_name'] 
        last_name= request.form['last_name']
        found_location= request.form['found_location']
        email= request.form['email'] 
        phone_num= request.form['phone_num'] 
        date_found= request.form['date_found']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM contacts WHERE first_name = % s', (first_name,))
        contact= cursor.fetchone()
        if contact:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', first_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', last_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', found_location):
            msg= 'Invalid location'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        elif not re.match(r'[A-Za-z0-9]+', phone_num):
            msg= 'Invalid locatin'
        elif not re.match(r'[A-Za-z0-9]+', date_found):
            msg= 'Invalid data'
        else:
            cursor.execute('INSERT INTO contacts VALUES ( %s, %s, %s, %s, %s, %s)', (first_name, last_name, found_location, email, phone_num, date_found, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    return render_template('foundpage.html', msg= msg)

    
       


@app.route("/major", methods= ['GET', 'POST'])
def major():    
    global data
    msg = ''
    if request.method== 'POST' and 'srno' in request.form and 'relation' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'age' in request.form and 'identity_mark' in request.form and 'date_lost' in request.form and 'address' in request.form and 'pincode' in request.form and 'city' in request.form and 'phone_num' in request.form and 'email' in request.form:
        srno= request.form['srno']
        relation= request.form['relation']
        first_name= request.form['first_name'] 
        last_name= request.form['last_name']
        age= request.form['age']
        identity_mark= request.form['identity_mark']
        date_lost= request.form['date_lost']
        address= request.form['address']
        pincode= request.form['pincode']
        city= request.form['city'] 
        phone_num= request.form['phone_num'] 
        email= request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        '''cursor.execute('SELECT * FROM lost WHERE first_name = % s, srno = %s, relation =  %s, last_name = %s, age = %s, identity_mark = %s, date_lost= %s, address = %s, pincode = %s, city = %s, phone_num = %s, email= %s',(first_name, srno, relation, last_name, age, identity_mark, date_lost, address, pincode, city, phone_num, email) )'''
        cursor.execute('SELECT * FROM lost WHERE first_name = % s', (first_name,))
        lol= cursor.fetchone()
        if lol:
            msg= 'Entry already exists !'
        elif not re.match(r'[A-Za-z0-9]+', srno):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', relation):
            msg= 'Invalid relation'
        elif not re.match(r'[A-Za-z0-9]+', first_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', last_name):
            msg= 'Invalid name'
        elif not re.match(r'[A-Za-z0-9]+', age):
            msg= 'Invalid age'
        elif not re.match(r'[A-Za-z0-9]+', identity_mark):
            msg= 'Invalid identity mark'
        elif not re.match(r'[A-Za-z0-9]+', date_lost):
            msg= 'Invalid date'
        elif not re.match(r'[A-Za-z0-9]+', address):
            msg= 'Invalid address'
        elif not re.match(r'[A-Za-z0-9]+', pincode):
            msg= 'Invalid pincode'
        elif not re.match(r'[A-Za-z0-9]+', city):
            msg= 'Invalid city'
        elif not re.match(r'[A-Za-z0-9]+', phone_num):
            msg= 'Invalid number'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg= 'Invalid email'
        
        else:
            cursor.execute('INSERT INTO lost VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (srno, relation, first_name, last_name, age, identity_mark, date_lost,  address, pincode, city,phone_num,  email, ))
            mysql.connection.commit()
            msg= 'Succesfully entered the data'
    elif request.method == 'POST':
        msg= 'Please fill out form'
    return render_template('adminlogin.html', msg= msg)
       


@app.route("/important")
def imp():
    
       return render_template('mainpage.html')


@app.route("/index")
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM lost")
    data= cur.fetchall()
    cur.close()
    return render_template('index.html', lost = data)
app.run(debug=True)

@app.route("/fdet")
def fdet():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    data = cur.fetchall()
    cur.close()
    return render_template('fdet.html', contacts = data)
app.run(debug=True)




@app.route("/mp", methods = ['GET', 'POST'])
def mp():
    
    '''if request.method == 'POST' and 'last_name' in request.form and 'age' in request.form and 'identity_mark' in request.form and 'date_lost' in request.form and 'address' in request.form and 'pincode' in request.form and 'city' in request.form and 'phone_num' in request.form and 'email' in request.form:
     srno= request.form['srno']
     relation= request.form['relation']
     first_name= request.form['first_name'] 
     last_name= request.form['last_name']
     age= request.form['age']
     identity_mark= request.form['identity_mark']
     date_lost= request.form['date_lost']
     address= request.form['address']
     pincode= request.form['pincode']
     city= request.form['city'] 
     phone_num= request.form['phone_num'] 
     email= request.form['email']
     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
     cursor.execute('SELECT * FROM lost WHERE first_name = % s, srno = %s, relation =  %s, last_name = %s, age = %s, identity_mark = %s, date_lost= %s, address = %s, pincode = %s, city = %s, phone_num = %s, email= %s',(first_name, srno, relation, last_name, age, identity_mark, date_lost, address, pincode, city, phone_num, email) )
     lol= cursor.fetchall()'''
    return render_template('view.html' )
app.run(debug=True)