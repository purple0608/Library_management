from flask import Flask,render_template,request,url_for,redirect
from jinja2 import FileSystemLoader
import pandas as pd
import matplotlib
app=Flask(__name__)
@app.route('/')
def front():
    return render_template('front.html')
@app.route('/Admin')
def Admin():
    return render_template('Admin.html')
@app.route('/librarian')
def librarian():
    return render_template('librarian.html')
@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/continuing')
def continuing():
    return render_template('continuing.html')

if __name__ == '__main__':
    app.run()
