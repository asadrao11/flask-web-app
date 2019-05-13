from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://phpmyadminuser:Pakistan12345@@localhost/cloudexperts'
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    sno, name, phone_num, email, msg, date
    '''

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    phone_num = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(15), nullable=True)



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        # Indentation check
        '''Add entry to the database'''

        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        ''' sno, name, phone_num, email, msg, date '''
        entry = Contacts(name=name, phone_num=phone, email=email, date=datetime.now(), msg=message)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/post")
def post():
    return render_template('post.html')

app.run(debug = True)